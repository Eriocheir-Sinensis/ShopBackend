FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /code/www
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt

