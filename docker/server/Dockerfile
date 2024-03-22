FROM python:3.11

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt


COPY . /app/
COPY .env.docker .env
RUN export PYTHONPATH=$PWD

CMD ["python", "manage.py", "migrate"]
CMD ["uvicorn", "DjangoNinjaTaskScheduler.asgi:application", "--host", "0.0.0.0", "--port", "80", "--reload"]
