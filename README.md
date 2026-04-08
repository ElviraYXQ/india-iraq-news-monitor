# 印度&伊拉克每日新闻监控系统

每天自动搜索印度和伊拉克市场的电商、科技、AI、互联网相关新闻，并发送到飞书。

## 🚀 快速开始（5分钟配置）

### 第一步：Fork 这个仓库

1. 点击页面右上角的 **Fork** 按钮
2. 创建到你自己的 GitHub 账号下

### 第二步：获取 Serper API Key（免费新闻搜索）

1. 访问 https://serper.dev
2. 点击 **Sign up** 注册账号（可以用 Google 账号登录）
3. 登录后，在 Dashboard 页面找到你的 **API Key**
4. 复制这个 API Key（免费额度：每月2500次搜索）

### 第三步：获取飞书应用凭证

你已经有飞书应用了，使用现有的配置即可：

- **App ID**: `cli_a9418088f5b8dcb1`
- **App Secret**: 需要从飞书开发者后台获取
- **User ID**: `ou_cc38ac881bcf17d997f0cad7d9a9a621` (你的 Open ID)

#### 如何获取 App Secret：

1. 访问 https://open.feishu.cn/app
2. 找到应用 `cli_a9418088f5b8dcb1`
3. 进入「凭证与基础信息」页面
4. 复制 **App Secret**

#### 确认应用权限：

确保应用有以下权限（应该已经开通）：
- ✅ `im:message`（发送消息）
- ✅ `im:message:send_as_bot`（以应用身份发消息）

### 第四步：在 GitHub 配置密钥

1. 在你 Fork 的仓库中，点击 **Settings**
2. 左侧菜单选择 **Secrets and variables** → **Actions**
3. 点击 **New repository secret**，依次添加以下4个密钥：

| 密钥名称 | 值 | 说明 |
|---------|---|------|
| `SERPER_API_KEY` | 你的 Serper API Key | 从 serper.dev 获取 |
| `LARK_APP_ID` | `cli_a9418088f5b8dcb1` | 飞书应用ID |
| `LARK_APP_SECRET` | 你的 App Secret | 从飞书开发者后台获取 |
| `LARK_USER_ID` | `ou_cc38ac881bcf17d997f0cad7d9a9a621` | 你的飞书 Open ID |

**添加方式：**
- 点击 **New repository secret**
- Name: 填写密钥名称（如 `SERPER_API_KEY`）
- Secret: 粘贴对应的值
- 点击 **Add secret**
- 重复4次，添加全部4个密钥

### 第五步：启用 GitHub Actions

1. 在你的仓库中，点击 **Actions** 标签
2. 如果看到提示，点击 **I understand my workflows, go ahead and enable them**
3. 找到 **Daily India & Iraq News Monitor** 工作流
4. 点击 **Enable workflow**

### 第六步：测试运行

1. 在 **Actions** 页面，点击左侧的 **Daily India & Iraq News Monitor**
2. 点击右侧的 **Run workflow** 下拉按钮
3. 点击绿色的 **Run workflow** 按钮
4. 等待约1-2分钟，查看运行结果
5. 检查你的飞书是否收到消息

---

## ✅ 完成！

配置完成后：
- ✅ 每天北京时间 **9:00** 自动运行
- ✅ 自动搜索印度和伊拉克的相关新闻
- ✅ 自动发送到你的飞书
- ✅ 完全免费
- ✅ 长期稳定运行

---

## 📊 监控内容

### 关注市场
- 🇮🇳 印度
- 🇮🇶 伊拉克

### 关注领域
- 电商和零售
- 互联网和科技
- AI和数字化
- 经济和民生
- 女性消费
- 时尚行业
- 物流支付

### 每日产出
每天早上9点，你会收到一条飞书消息，格式如下：

```
📰 每日市场新闻速递 - 2026-04-08

🇮🇳 印度市场

1. 印度电商巨头推出AI购物助手...
   [Flipkart launches AI shopping assistant](https://example.com)

2. 印度数字支付用户突破10亿...
   [India's digital payment users cross 1 billion](https://example.com)

🇮🇶 伊拉克市场

1. 伊拉克政府推动电商发展计划...
   [Iraq government promotes e-commerce development](https://example.com)

---
💡 关注领域：电商、科技、AI、互联网、民生、女性消费
```

---

## 🔧 常见问题

### Q: 为什么没有收到消息？

1. 检查 GitHub Actions 是否运行成功
   - 进入 **Actions** 页面查看最近的运行记录
   - 如果显示红色❌，点击查看错误日志

2. 检查密钥是否正确
   - Settings → Secrets and variables → Actions
   - 确认4个密钥都已添加且值正确

3. 检查飞书应用权限
   - 确保应用有 `im:message` 权限
   - 确保应用已启用

### Q: 如何修改运行时间？

编辑 `.github/workflows/daily-news.yml` 文件中的 cron 表达式：

```yaml
schedule:
  # 每天北京时间9:00 = UTC 1:00
  - cron: '0 1 * * *'
```

修改为你想要的时间，例如：
- 北京时间 8:00: `'0 0 * * *'`
- 北京时间 10:00: `'0 2 * * *'`
- 北京时间 18:00: `'0 10 * * *'`

### Q: 如何修改搜索关键词？

编辑 `news_monitor.py` 文件中的 `queries` 列表，添加或修改搜索关键词。

### Q: Serper API 免费额度用完了怎么办？

免费额度：每月2500次搜索
- 本脚本每天约使用 8-10 次搜索
- 理论上每月免费额度足够使用

如果用完：
1. 升级到付费计划（$50/月 5000次）
2. 或者使用其他新闻API（需要修改代码）

### Q: 新闻质量不满意？

可以调整以下参数：
1. 修改搜索关键词（`news_monitor.py` 中的 `queries`）
2. 调整相关性过滤条件（`is_relevant` 函数）
3. 增加或减少返回的新闻数量

---

## 📝 技术说明

### 架构
- **运行环境**: GitHub Actions (免费)
- **新闻搜索**: Serper API (Google News)
- **消息推送**: 飞书 Open API
- **编程语言**: Python 3.11

### 文件说明
- `news_monitor.py`: 主程序脚本
- `.github/workflows/daily-news.yml`: GitHub Actions 工作流配置
- `requirements.txt`: Python 依赖
- `README.md`: 本说明文档

---

## 🛠️ 高级定制

### 添加其他市场

在 `news_monitor.py` 中添加新的函数：

```python
def collect_xxx_news():
    queries = [
        "XXX e-commerce OR online shopping",
        "XXX internet OR technology OR AI",
    ]
    # 复制 collect_india_news 的逻辑
    ...
```

### 发送到多个人

修改 `send_to_lark` 函数，循环发送到多个 user_id。

### 保存历史记录

添加代码将新闻保存到飞书云文档或 GitHub 仓库。

---

## 📄 许可证

MIT License

---

## 💡 支持

如有问题，请：
1. 检查本 README 的「常见问题」部分
2. 查看 GitHub Actions 运行日志
3. 联系技术支持

---

**祝使用愉快！🎉**
