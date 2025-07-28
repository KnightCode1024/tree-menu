# Древовидное меню для Django

[![Python](https://img.shields.io/badge/Python-3.12%2B-blue)](https://python.org)
[![Django](https://img.shields.io/badge/Django-5.2%2B-green)](https://djangoproject.com)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-17%2B-blue)](https://www.postgresql.org)
[![Docker](https://img.shields.io/badge/Docker-24.0%2B-blue)](https://www.docker.com)

## Требования
- Python 3.12
- Наличие Docker Desktop 

## 🌟 О приложение
![](example.png)
Был разработан шаблонный тег `draw_menu` для древовидного отображения меню. Тег принимает название меню `Menu.name`

```html
 <div>
    {% draw_menu 'menu' %}
 </div>
```

## 🛠 Технологический стек
- Django 
- PostgreSQL 
- Bootstrap 
- Docker

## 🚀 Быстрый старт с Docker

1. Клонируйте репозиторий:
```bash
git clone https://github.com/KnightCode1024/tree-menu.git
cd tree-menu
```

2. Сборка и запуск приложение:
```bash
    docker-compose up --build
```

3. Посмотреть результат на http://127.0.0.1:8000/
