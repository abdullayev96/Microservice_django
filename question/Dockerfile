# FROM python:3.10
#
# ENV PYTHONUNBUFFERED 1
#
# RUN mkdir /app
# WORKDIR /app
# COPY  requirements.txt /app/requirements.txt
# RUN pip3 install -r requirements.txt
#
#
# COPY . /app
#
# CMD  python manage.py runserver  127.0.0.1:8000


FROM python:3.11

ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app


EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]