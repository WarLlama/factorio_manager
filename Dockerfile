FROM python:2.7

EXPOSE 8000
COPY . /var/app
RUN pip install -r /var/app/requirements.txt

CMD python /var/app/factorio_manager/manage.py runserver 0.0.0.0:8000