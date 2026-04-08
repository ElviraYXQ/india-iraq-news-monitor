# 📋 快速配置检查清单

## ✅ 需要准备的信息

### 1. Serper API Key（新闻搜索服务）

**获取步骤：**
1. 打开浏览器访问：https://serper.dev
2. 点击右上角 **Sign up** 或 **Get API Key**
3. 使用 Google 账号登录（或邮箱注册）
4. 登录后自动跳转到 Dashboard
5. 复制显示的 **API Key**（格式类似：`abc123def456...`）

**费用：**
- ✅ 免费额度：2500次/月
- ✅ 本脚本每天约用8-10次，足够使用

---

### 2. 飞书应用凭证

你已经有飞书应用配置，直接使用即可：

#### App ID
```
cli_a9418088f5b8dcb1
```

#### App Secret（需要获取）
**获取步骤：**
1. 访问：https://open.feishu.cn/app 或 https://open.larksuite.com/app
2. 登录你的飞书账号
3. 在应用列表中找到应用（可能名为 "lark-cli" 或其他名称）
4. 点击进入应用详情
5. 左侧菜单选择「凭证与基础信息」
6. 找到 **App Secret**，点击「查看」或「复制」

**如果找不到应用：**
- 联系你们的飞书管理员
- 或者询问之前配置 lark-cli 的同事

#### User ID
```
ou_cc38ac881bcf17d997f0cad7d9a9a621
```
（这是你的飞书 Open ID，无需修改）

---

### 3. 确认应用权限

你的应用需要有以下权限：

- ✅ `im:message` - 获取与发送单聊、群组消息
- ✅ `im:message:send_as_bot` - 以应用的身份发消息

**检查方式：**
1. 在飞书开发者后台进入应用
2. 左侧菜单选择「权限管理」
3. 搜索 "消息" 或 "message"
4. 确认上述权限已开通

**如果没有权限：**
- 点击「添加权限」
- 搜索并添加上述两个权限
- 点击「保存」
- 可能需要管理员审批

---

## 🚀 GitHub 配置步骤

### 步骤1：上传代码到 GitHub

**方式A：使用 GitHub 网页版（推荐）**

1. 访问 https://github.com/new 创建新仓库
2. Repository name: `india-iraq-news-monitor`
3. Description: `Daily India & Iraq market news monitoring`
4. 选择 **Private**（私有仓库）
5. ❌ 不要勾选 "Initialize this repository with a README"
6. 点击 **Create repository**
7. 在你的电脑终端运行：

```bash
cd ~/india-iraq-news-monitor
git remote add origin https://github.com/你的用户名/india-iraq-news-monitor.git
git branch -M main
git push -u origin main
```

**方式B：使用 GitHub Desktop（如果你安装了）**

1. 打开 GitHub Desktop
2. File → Add Local Repository
3. 选择 `/Users/yixiqian/india-iraq-news-monitor`
4. 点击 "Publish repository"
5. 选择 Private
6. 点击 "Publish Repository"

---

### 步骤2：配置 GitHub Secrets

1. 在 GitHub 仓库页面，点击 **Settings**
2. 左侧菜单：**Secrets and variables** → **Actions**
3. 点击 **New repository secret**

**依次添加4个密钥：**

| 名称 | 值 | 从哪里获取 |
|-----|---|---------|
| `SERPER_API_KEY` | 你的 Serper API Key | 从 serper.dev 复制 |
| `LARK_APP_ID` | `cli_a9418088f5b8dcb1` | 直接复制这个值 |
| `LARK_APP_SECRET` | 你的 App Secret | 从飞书开发者后台复制 |
| `LARK_USER_ID` | `ou_cc38ac881bcf17d997f0cad7d9a9a621` | 直接复制这个值 |

**添加每个密钥的操作：**
1. 点击 **New repository secret**
2. Name: 输入上表中的"名称"
3. Secret: 粘贴对应的"值"
4. 点击 **Add secret**
5. 重复4次

---

### 步骤3：启用 GitHub Actions

1. 在仓库页面，点击 **Actions** 标签
2. 看到提示时，点击 **I understand my workflows, go ahead and enable them**
3. 左侧找到 **Daily India & Iraq News Monitor**
4. 如果看到"This workflow is disabled"，点击 **Enable workflow**

---

### 步骤4：测试运行

1. 在 **Actions** 页面
2. 点击左侧的 **Daily India & Iraq News Monitor**
3. 点击右侧的 **Run workflow** 按钮（绿色下拉框）
4. 再次点击绿色的 **Run workflow** 确认
5. 等待约1-2分钟
6. 刷新页面，查看运行状态
7. 如果显示绿色✅，表示成功
8. 检查你的飞书是否收到消息

**如果失败（红色❌）：**
1. 点击失败的运行记录
2. 查看错误日志
3. 通常是因为密钥配置错误或权限不足
4. 检查上述配置步骤

---

## 🎉 完成！

配置成功后：
- ✅ 每天北京时间 9:00 自动运行
- ✅ 自动发送新闻到飞书
- ✅ 完全免费
- ✅ 无需维护

---

## 📞 需要帮助？

### 常见错误

**错误1: "401 Unauthorized"**
- 原因：App Secret 或 App ID 错误
- 解决：重新检查飞书开发者后台的凭证

**错误2: "permission denied"**
- 原因：应用缺少消息权限
- 解决：在飞书开发者后台添加 `im:message` 权限

**错误3: "API key invalid"**
- 原因：Serper API Key 错误
- 解决：重新从 serper.dev 复制 API Key

**错误4: "user not found"**
- 原因：User ID 错误
- 解决：确认 User ID 是否正确

---

## 📱 联系方式

如果遇到问题：
1. 截图错误日志
2. 发送给技术支持
3. 或者联系配置此系统的人

---

**预计配置时间：5-10分钟**
**难度：⭐⭐ (简单)**
