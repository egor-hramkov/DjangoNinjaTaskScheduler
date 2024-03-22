# Запуск сервера:
uvicorn DjangoNinjaTaskScheduler.asgi:application --reload

# Запуск Celery и Flower
- celery -A celery_layer.tasks worker --loglevel=INFO --pool=solo
- celery -A celery_layer.tasks flower


# docker
- copy .env.example to .env.docker
- cd docker
- docker compose up -d
