FROM python:2.7

EXPOSE 8000
ADD requirements.txt /tmp/requirements.txt
WORKDIR /var/app
RUN pip install -r /tmp/requirements.txt

COPY factorio_manager /var/app

CMD python manage.py runserver 0.0.0.0:8000