FROM python:3.10

RUN pip install --upgrade pip

ENV PYTHONUNBUFFERED 1
RUN mkdir /code

WORKDIR /code
COPY . /code/

RUN pip install -r requirements/deb.txt

CMD ["gunicorn","-c", "config/gunicorn/conf.py","--bind", ":8000", "dental_copilot.wsgi:application"]

