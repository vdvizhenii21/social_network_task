FROM python:3.9.7-slim
WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD gunicorn social_network_task.wsgi:application --bind 0.0.0.0:8000 