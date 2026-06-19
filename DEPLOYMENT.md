# 部署说明

这个项目是前后端分离：

- 后端：Django，提供后台管理和注册/登录 API。
- 前端：Vue + Vite，负责父亲节网站页面。

## 推荐方案

最省事的组合：

- 后端部署到 Render Web Service。
- 前端部署到 Vercel 或 Render Static Site。

如果你想少切平台，也可以前端和后端都放 Render，并使用项目根目录的 `render.yaml`。

## 后端上线

1. 把项目推送到 GitHub。
2. 在 Render 新建 Web Service，选择这个仓库。
3. 后端配置：
   - Root Directory：留空
   - Build Command：`pip install -r requirements.txt && python manage.py collectstatic --no-input && python manage.py migrate`
   - Start Command：`gunicorn config.wsgi:application`
4. 设置环境变量：
   - `DJANGO_DEBUG=False`
   - `DJANGO_SECRET_KEY=一串很长的随机字符串`
   - `DJANGO_ALLOWED_HOSTS=你的后端域名`
   - `DJANGO_CSRF_TRUSTED_ORIGINS=https://你的后端域名`
   - `FRONTEND_URL=https://你的前端域名`
   - `CORS_ALLOWED_ORIGIN=https://你的前端域名`

后端部署成功后，访问：

```text
https://你的后端域名/api/health/
```

看到 `{"success": true, "message": "ok"}` 就说明后端正常。

## 前端上线到 Vercel

1. 在 Vercel 新建 Project，导入同一个 GitHub 仓库。
2. 设置：
   - Root Directory：`frontend`
   - Framework Preset：Vite
   - Build Command：`npm run build`
   - Output Directory：`dist`
3. 设置环境变量：
   - `VITE_API_BASE_URL=https://你的后端域名`

部署后，把前端域名填回后端的：

- `FRONTEND_URL`
- `CORS_ALLOWED_ORIGIN`

然后重新部署后端。

## 前端上线到 Render

如果使用 `render.yaml`，Render 会同时创建：

- `fathers-day-backend`
- `fathers-day-frontend`

创建后需要把 `render.yaml` 里的示例域名改成 Render 实际生成的域名，再重新部署一次。

## 关于数据库

当前项目使用 SQLite。它适合这个小型礼物网站。

注意：部分免费云平台的文件系统可能会在重启或重新部署后重置。如果你希望注册表单数据长期保留，建议后续改成 PostgreSQL。
