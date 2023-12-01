# BusinessBot
## Запуск

Склонируйте репозиторий на локальную машину.

В файле `docker-compose.yml` измените константы под себя.

Запустите Docker-контейнер.
```
docker-compose up --build -d
```
Накатите миграции.
```
docker exec business_bot alembic upgrade head
```
Заполните БД.
```
docker exec business_bot python -m app.fill_message_template_table
```
Запустите бота.
```
exec business_bot python -m app.main
```

