![example workflow](https://github.com/Kiselev1988/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

# Проект YaMDb_Final

Проект доступен по адресу http://51.250.25.202/api/v1/   http://51.250.25.202/redoc/
### Клонировать репозиторий
git clone https://github.com/Kiselev1988/yamdb_final.git

### Создать файл .env с содержанием:

DB_ENGINE=django.db.backends.postgresql,
DB_NAME=postgres,
POSTGRES_USER=postgres,
POSTGRES_PASSWORD=postgres,
DB_HOST=db,
DB_PORT=5432

### Создать контейнеры :

docker-compose up --build

### Выполнить миграции :

docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate

### Скомпоновать статику :

docker-compose exec web python manage.py collectstatic --no-input

### Загрузить БД тестовыми данными :

docker-compose exec web python manage.py loaddata fixtures.sql

### Использованные технологии:
- Python 3
- Django
- Django REST framework
- PostgeSQL
- Nginx
- Docker-composer

# Автор:
- Никита Киселев. <https://github.com/Kiselev1988>



