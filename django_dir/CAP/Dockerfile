FROM python:3.10-slim
ENV PYTHONPATH /home/devu/PycharmProjects/aplicationForTheCompanyAndPartners/django_dir/CAP
COPY reqs.txt /temp/reqs.txt
COPY CAP /CAP

WORKDIR CAP

RUN pip install -r /temp/reqs.txt

CMD python manage.py makemigrations \
    && python manage.py migrate \
    && python manage.py runserver 0.0.0.0:8000