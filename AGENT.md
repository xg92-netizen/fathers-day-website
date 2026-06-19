# AGENT.md

## Project Overview

This project is a Django + Vue application.

- Backend: Django 4.2.30
- Admin UI: django-simpleui 2026.1.13
- Frontend: Vue 3 + Vite
- Database: SQLite (`db.sqlite3`)
- Python virtual environment: `.venv`
- Django project package: `config`
- Django app: `core`
- Vue app directory: `frontend`

## Important Paths

- Django settings: `config/settings.py`
- Django URLs: `config/urls.py`
- Django app: `core/`
- Vue frontend: `frontend/`
- Python dependencies: `requirements.txt`
- Vue dependencies: `frontend/package.json`

## Environment

Always activate the project virtual environment before running backend or frontend commands:

```bash
source .venv/bin/activate
```

The virtual environment also contains the Node/npm toolchain installed with `nodeenv`.

## Run The Project

Start Django:

```bash
source .venv/bin/activate
python manage.py runserver 127.0.0.1:8000
```

Start Vue:

```bash
source .venv/bin/activate
cd frontend
npm run dev -- --host 127.0.0.1
```

Local URLs:

- Vue frontend: `http://127.0.0.1:5173/`
- Django admin: `http://127.0.0.1:8000/admin/`
- Django root: `http://127.0.0.1:8000/` redirects to the Vue dev server.

## Admin Account

Existing superuser:

- Username: `gaoxiaoya`
- Email: `1737486800@qq.com`
- Nickname stored in `first_name`: `wqok`

## Current Django Configuration

- `simpleui` is registered before `django.contrib.admin` in `INSTALLED_APPS`.
- `core` is registered in `INSTALLED_APPS`.
- Language is set to Simplified Chinese: `LANGUAGE_CODE = 'zh-hans'`.
- Time zone is set to Shanghai: `TIME_ZONE = 'Asia/Shanghai'`.

## Current Frontend Configuration

The Vue app was created with Vite and lives in `frontend/`.

Useful commands:

```bash
cd frontend
npm run dev
npm run build
npm run preview
```

The current Vue entry files are:

- `frontend/src/main.js`
- `frontend/src/App.vue`
- `frontend/src/style.css`

## Validation Commands

Before finishing backend changes, run:

```bash
source .venv/bin/activate
python manage.py check
```

Before finishing frontend changes, run:

```bash
source .venv/bin/activate
cd frontend
npm run build
```

## Development Notes

- Keep Django admin available at `/admin/`.
- Keep the Vue frontend as the public-facing site.
- Avoid committing `.venv/`, `frontend/node_modules/`, or `frontend/dist/`.
- If Python packages change, update `requirements.txt` with:

```bash
source .venv/bin/activate
python -m pip freeze > requirements.txt
```

- If Vue packages change, keep `frontend/package-lock.json` updated by using npm from inside the activated `.venv`.
