#!/usr/bin/env python3
"""
印度和伊拉克每日新闻监控脚本
每天自动搜索相关新闻并发送到飞书
"""

import os
import requests
from datetime import datetime, timedelta
import json


def search_news(query, days=1):
    """使用Serper API搜索新闻"""
    api_key = os.environ.get('SERPER_API_KEY')

    if not api_key:
        print("警告: SERPER_API_KEY 未设置，使用模拟数据")
        return []

    url = "https://google.serper.dev/news"

    payload = json.dumps({
        "q": query,
        "num": 10,
        "tbs": f"qdr:d{days}"  # 搜索过去N天的新闻
    })

    headers = {
        'X-API-KEY': api_key,
        'Content-Type': 'application/json'
    }

    try:
        response = requests.post(url, headers=headers, data=payload, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data.get('news', [])
    except Exception as e:
        print(f"搜索失败 [{query}]: {str(e)}")
        return []


def is_relevant(title, snippet, keywords):
    """判断新闻是否相关"""
    text = (title + " " + snippet).lower()

    # 排除明显不相关的内容
    exclude_keywords = ['cricket', 'bollywood', 'film', 'movie', 'sports', 'football']
    if any(kw in text for kw in exclude_keywords):
        return False

    # 必须包含至少一个关键词
    return any(kw.lower() in text for kw in keywords)


def collect_india_news():
    """收集印度相关新闻"""
    queries = [
        "India e-commerce OR online shopping OR digital payment",
        "India internet OR technology OR AI OR startup",
        "India retail OR consumer OR fashion OR women",
        "India mobile commerce OR fintech"
    ]

    keywords = [
        'e-commerce', 'ecommerce', 'online shopping', 'digital payment',
        'internet', 'ai', 'technology', 'consumer', 'retail',
        'fashion', 'women', 'mobile', 'fintech', 'startup'
    ]

    all_news = []
    seen_urls = set()

    for query in queries:
        news_items = search_news(query)
        for item in news_items:
            url = item.get('link', '')
            if url and url not in seen_urls:
                title = item.get('title', '')
                snippet = item.get('snippet', '')

                if is_relevant(title, snippet, keywords):
                    seen_urls.add(url)
                    all_news.append({
                        'title': title,
                        'snippet': snippet,
                        'url': url,
                        'date': item.get('date', '')
                    })

    return all_news[:15]  # 最多返回15条


def collect_iraq_news():
    """收集伊拉克相关新闻"""
    queries = [
        "Iraq e-commerce OR online shopping OR digital payment",
        "Iraq internet OR technology OR AI OR startup",
        "Iraq retail OR consumer OR fashion OR women",
        "Iraq mobile commerce OR economy"
    ]

    keywords = [
        'e-commerce', 'ecommerce', 'online shopping', 'digital payment',
        'internet', 'ai', 'technology', 'consumer', 'retail',
        'fashion', 'women', 'mobile', 'fintech', 'economy'
    ]

    all_news = []
    seen_urls = set()

    for query in queries:
        news_items = search_news(query)
        for item in news_items:
            url = item.get('link', '')
            if url and url not in seen_urls:
                title = item.get('title', '')
                snippet = item.get('snippet', '')

                if is_relevant(title, snippet, keywords):
                    seen_urls.add(url)
                    all_news.append({
                        'title': title,
                        'snippet': snippet,
                        'url': url,
                        'date': item.get('date', '')
                    })

    return all_news[:15]  # 最多返回15条


def format_news_message(india_news, iraq_news):
    """格式化新闻消息"""
    today = datetime.now().strftime('%Y-%m-%d')

    message = f"📰 **每日市场新闻速递 - {today}**\n\n"

    # 印度新闻
    message += "🇮🇳 **印度市场**\n\n"
    if india_news:
        for i, news in enumerate(india_news, 1):
            snippet = news['snippet'][:100] + "..." if len(news['snippet']) > 100 else news['snippet']
            message += f"{i}. {snippet}\n   [{news['title']}]({news['url']})\n\n"
    else:
        message += "今日暂无重要相关新闻\n\n"

    # 伊拉克新闻
    message += "🇮🇶 **伊拉克市场**\n\n"
    if iraq_news:
        for i, news in enumerate(iraq_news, 1):
            snippet = news['snippet'][:100] + "..." if len(news['snippet']) > 100 else news['snippet']
            message += f"{i}. {snippet}\n   [{news['title']}]({news['url']})\n\n"
    else:
        message += "今日暂无重要相关新闻\n\n"

    message += "---\n💡 *关注领域：电商、科技、AI、互联网、民生、女性消费*"

    return message


def send_to_lark(message):
    """发送消息到飞书"""
    user_id = os.environ.get('LARK_USER_ID')  # ou_cc38ac881bcf17d997f0cad7d9a9a621
    app_id = os.environ.get('LARK_APP_ID')
    app_secret = os.environ.get('LARK_APP_SECRET')

    if not all([user_id, app_id, app_secret]):
        print("错误: 飞书配置不完整")
        print(f"LARK_USER_ID: {'✓' if user_id else '✗'}")
        print(f"LARK_APP_ID: {'✓' if app_id else '✗'}")
        print(f"LARK_APP_SECRET: {'✓' if app_secret else '✗'}")
        return False

    # 获取 tenant_access_token
    auth_url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
    auth_payload = {
        "app_id": app_id,
        "app_secret": app_secret
    }

    try:
        auth_response = requests.post(auth_url, json=auth_payload, timeout=10)
        auth_response.raise_for_status()
        access_token = auth_response.json().get('tenant_access_token')

        if not access_token:
            print("错误: 获取access_token失败")
            return False

        # 发送消息
        send_url = "https://open.feishu.cn/open-apis/im/v1/messages"
        params = {"receive_id_type": "open_id"}
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }

        payload = {
            "receive_id": user_id,
            "msg_type": "text",
            "content": json.dumps({"text": message})
        }

        send_response = requests.post(send_url, params=params, headers=headers, json=payload, timeout=10)
        send_response.raise_for_status()

        result = send_response.json()
        if result.get('code') == 0:
            print("✓ 消息发送成功")
            return True
        else:
            print(f"✗ 发送失败: {result}")
            return False

    except Exception as e:
        print(f"✗ 发送到飞书失败: {str(e)}")
        return False


def main():
    """主函数"""
    print("=" * 60)
    print("开始执行每日新闻监控任务")
    print(f"时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)

    # 收集新闻
    print("\n1️⃣  正在收集印度市场新闻...")
    india_news = collect_india_news()
    print(f"   找到 {len(india_news)} 条相关新闻")

    print("\n2️⃣  正在收集伊拉克市场新闻...")
    iraq_news = collect_iraq_news()
    print(f"   找到 {len(iraq_news)} 条相关新闻")

    # 格式化消息
    print("\n3️⃣  正在格式化消息...")
    message = format_news_message(india_news, iraq_news)

    # 发送到飞书
    print("\n4️⃣  正在发送到飞书...")
    success = send_to_lark(message)

    if success:
        print("\n✅ 任务执行成功！")
    else:
        print("\n❌ 任务执行失败")
        # 打印消息用于调试
        print("\n生成的消息内容:")
        print(message)

    print("=" * 60)


if __name__ == "__main__":
    main()
