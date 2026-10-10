# 项目说明（acnet.md）

> 一个基于 Django 5.2 + Vue 3 的前后端分离示例项目。
> Django 负责 REST API 与后台管理（SimpleUI），Vue 3 + Vite 负责前端页面。

## 1. 项目简介

- 后端框架：Django 5.2.18 + Django REST Framework 3.18.3
- 前端框架：Vue 3 + Vite + axios
- 数据库：MySQL 8.0（数据库名 mysite）
- 后台管理：django-simpleui（中文界面）
- 跨域方案：django-cors-headers（开发环境）

## 2. 技术栈与版本

| 类型 | 名称 | 版本 |
| --- | --- | --- |
| 语言 | Python | 3.12.0 |
| 后端 | Django | 5.2.18 |
| 数据库驱动 | mysqlclient | 2.3.0 |
| API | djangorestframework | 3.18.3 |
| 后台 | django-simpleui | 2026.1.13 |
| 跨域 | django-cors-headers | 4.9.0 |
| 前端 | Vue | 3.5.x |
| 构建 | Vite | 8.3.x |
| 请求 | axios | 1.20.x |
| 运行环境 | Node.js / npm | 25.2.1 / 11.6.2 |

## 3. 架构说明

```
浏览器
   |
   +--> /            -> Vue 单页应用（frontend/dist/index.html）
   +--> /static/*    -> Vue 构建产物的 JS/CSS（frontend/dist）
   +--> /api/*       -> Django REST Framework 接口 -> MySQL 8.0
   +--> /admin/      -> Django 后台管理（SimpleUI 中文界面）
```

开发模式下，前端由 Vite 开发服务器（localhost:5173）提供，并通过代理将 /api 转发到 Django（127.0.0.1:8000），实现热更新与免跨域。

## 4. 目录结构

```
D:\我的codex
|-- .venv/                  # Python 虚拟环境
|-- mysite/                 # Django 项目配置包
|   |-- settings.py         # 全局配置（语言、时区、CORS、静态目录等）
|   |-- urls.py             # 路由：admin / api / Vue 入口
|   |-- wsgi.py             # WSGI 入口
|   `-- asgi.py             # ASGI 入口
|-- polls/                  # 示例应用
|   |-- views.py            # api_hello 示例接口
|   |-- urls.py             # 应用路由（当前为空）
|   `-- migrations/         # 数据库迁移
|-- frontend/               # Vue 3 + Vite 前端工程
|   |-- src/
|   |   |-- App.vue         # 主页面（调用 /api/hello/）
|   |   |-- main.js         # 入口
|   |   `-- style.css       # 全局样式
|   |-- public/             # 静态资源（favicon 等）
|   |-- dist/               # 生产构建产物（Django 托管）
|   |-- vite.config.js      # Vite 配置（/api 代理、端口 5173）
|   `-- package.json        # 前端依赖与脚本
|-- manage.py               # Django 命令行入口
|-- db.sqlite3              # 旧 SQLite 文件（已停用，现使用 MySQL）
|-- requirements.txt        # Python 依赖清单
`-- .gitignore              # Git 忽略规则
```

## 5. 环境要求

- 操作系统：Windows（当前开发环境）
- Python 3.12（虚拟环境位于 .venv）
- Node.js 20+ 与 npm（建议最新 LTS，当前 25.2.1）
- MySQL 8.0（当前 8.0.43，运行于 127.0.0.1:3306，root/root，数据库 mysite）

## 6. 快速开始

### 6.1 启动后端

```powershell
cd D:\我的codex
.\.venv\Scripts\Activate.ps1            # 若被策略拦截，先执行：Set-ExecutionPolicy -Scope Process Bypass
pip install -r requirements.txt          # 首次安装依赖
python manage.py migrate                 # 初始化数据库
python manage.py runserver               # 启动，默认 http://127.0.0.1:8000/
```

### 6.2 启动前端（开发模式，热更新）

```powershell
cd D:\我的codex\frontend
npm install                              # 首次安装依赖
npm run dev                              # 打开 http://localhost:5173/
```

### 6.3 构建前端（生产模式）

```powershell
cd D:\我的codex\frontend
npm run build                            # 产物输出到 frontend/dist，Django 直接托管
```

## 7. 接口文档

### GET /api/hello/

示例接口，返回一段问候数据。

请求：
```
GET http://127.0.0.1:8000/api/hello/
```

响应（200）：
```json
{
  "message": "你好，Vue！这条数据来自 Django API。",
  "framework": "Django 5.2 + Django REST Framework"
}
```

## 8. 后台管理

- 地址：http://127.0.0.1:8000/admin/
- 界面：django-simpleui（已启用，中文）
- 超级管理员：
  - 用户名：kymlcode
  - 密码：admin123（仅用于本地开发，部署前务必修改）
  - 邮箱：kymlcode@163.com

## 9. 关键配置说明（mysite/settings.py）

- LANGUAGE_CODE = "zh-hans"：默认语言为中文
- TIME_ZONE = "Asia/Shanghai"：时区为上海
- INSTALLED_APPS：已注册 simpleui、rest_framework、corsheaders、polls
- MIDDLEWARE：已加入 corsheaders.middleware.CorsMiddleware
- CORS_ALLOWED_ORIGINS：允许 http://127.0.0.1:5173 与 http://localhost:5173
- TEMPLATES DIRS：指向 frontend/dist（用于托管 Vue 构建产物）
- STATICFILES_DIRS：指向 frontend/dist（用于 /static/ 静态资源）
- DATABASES：默认使用 MySQL（ENGINE=django.db.backends.mysql，数据库 mysite，utf8mb4）

## 10. 常用命令汇总

| 操作 | 命令 |
| --- | --- |
| 启动后端 | python manage.py runserver |
| 启动前端开发 | cd frontend && npm run dev |
| 构建前端 | cd frontend && npm run build |
| 创建超级管理员 | python manage.py createsuperuser |
| 数据库迁移 | python manage.py makemigrations && python manage.py migrate |
| 运行检查 | python manage.py check |
| 导出依赖 | pip freeze > requirements.txt |
