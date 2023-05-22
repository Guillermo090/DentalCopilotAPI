FROM python:3.7

ENV PYTHONUNBUFFERED 1
RUN mkdir /code

WORKDIR /code
COPY . /code/

RUN pip install -r requirements_linux.txt

CMD ["gunicorn","-c", "configs/gunicorn/conf.py","--bind", ":8000", "--chdir","dental_copilot", "dental_copilot.wsgi:application"]

