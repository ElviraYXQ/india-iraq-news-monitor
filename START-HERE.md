# 🎯 给 Queenie 的配置总结

## 📦 项目已准备就绪

所有代码文件已创建在：`/Users/yixiqian/india-iraq-news-monitor/`

### 文件清单
- ✅ `news_monitor.py` - 主程序（搜索新闻+发送飞书）
- ✅ `.github/workflows/daily-news.yml` - GitHub自动化配置
- ✅ `requirements.txt` - Python依赖
- ✅ `README.md` - 完整说明文档
- ✅ `SETUP-GUIDE.md` - 快速配置指南（推荐先看这个）
- ✅ `.gitignore` - Git忽略文件

---

## 🔑 你需要准备的信息（2个）

### 1. Serper API Key（免费）
- 访问：https://serper.dev
- 用 Google 账号登录
- 复制 Dashboard 显示的 API Key
- **费用**：免费2500次/月（足够使用）

### 2. 飞书 App Secret
你的 App ID 已配置好：`cli_a9418088f5b8dcb1`

**获取 App Secret：**
1. 访问：https://open.feishu.cn/app
2. 找到你的应用（app id: cli_a9418088f5b8dcb1）
3. 进入「凭证与基础信息」
4. 复制 **App Secret**

---

## 📝 配置步骤（总共5步，约10分钟）

### 步骤1: 上传代码到 GitHub

```bash
# 在终端执行以下命令
cd ~/india-iraq-news-monitor

# 1. 在 GitHub 创建新仓库（访问 github.com/new）
#    - 仓库名: india-iraq-news-monitor
#    - 类型: Private
#    - 不要勾选 "Initialize with README"

# 2. 运行以下命令（替换 YOUR_USERNAME 为你的 GitHub 用户名）
git remote add origin https://github.com/YOUR_USERNAME/india-iraq-news-monitor.git
git branch -M main
git push -u origin main
```

### 步骤2: 在 GitHub 配置密钥

进入仓库 → Settings → Secrets and variables → Actions → New repository secret

添加4个密钥：

| 名称 | 值 |
|-----|---|
| `SERPER_API_KEY` | 从 serper.dev 获取 |
| `LARK_APP_ID` | `cli_a9418088f5b8dcb1` |
| `LARK_APP_SECRET` | 从飞书开发者后台获取 |
| `LARK_USER_ID` | `ou_cc38ac881bcf17d997f0cad7d9a9a621` |

### 步骤3: 启用 GitHub Actions

1. 仓库页面 → Actions 标签
2. 点击 "Enable workflow"

### 步骤4: 测试运行

1. Actions → Daily India & Iraq News Monitor
2. Run workflow → Run workflow
3. 等待1-2分钟
4. 检查飞书是否收到消息

### 步骤5: 完成！

之后每天北京时间 9:00 自动运行。

---

## 📖 详细文档

- **快速配置**：查看 `SETUP-GUIDE.md`（更详细的分步指南）
- **完整说明**：查看 `README.md`（功能、常见问题、技术说明）

---

## 🆘 需要帮助？

### 方式1：找技术同事
把这个文件夹(`~/india-iraq-news-monitor`)发给技术同事，让他们帮你配置。

### 方式2：远程协助
我可以一步步指导你操作（需要你告诉我每一步的结果）。

### 方式3：简化方案
如果觉得太复杂，可以回到「半自动方案」：
- 每天飞书提醒你
- 你回复一下
- 我立即执行搜索

---

## ⏱️ 预计时间

- **有技术背景**：5-10分钟
- **无技术背景但按步骤操作**：15-20分钟
- **让技术同事帮忙**：5分钟

---

## 🎁 配置成功后你将获得

- ✅ 每天自动监控印度、伊拉克市场新闻
- ✅ 覆盖电商、科技、AI、互联网、民生
- ✅ 中英文混合新闻源
- ✅ 每条新闻1-2句概述+详细链接
- ✅ 每天9:00准时发送到飞书
- ✅ 完全免费
- ✅ 长期稳定运行
- ✅ 无需维护

---

**下一步：打开 `SETUP-GUIDE.md` 开始配置！**
