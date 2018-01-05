# Original
#FROM praekeltcom/django-bootstrap:latest
#COPY . /var/praekelt/app
#RUN /var/praekelt/ve/bin/pip install -r /var/praekelt/app/requirements/requirements.txt
#RUN /var/praekelt/ve/bin/python /var/praekelt/app/manage.py collectstatic --noinput
#VOLUME /mnt/gluster/mobius-demo:/var/praekelt/media
#WORKDIR /var/praekelt/app
#CMD /root/startProject.sh

# 0.1
#FROM ubuntu:17.10
#WORKDIR /var/app/
#RUN apt-get update && apt-get install -y python-pip python-dev git libpq-dev python-virtualenv libjpeg-dev zlib1g-dev build-essential git-core libxslt1-dev
#COPY ./requirements /var/app/requirements/
#RUN pip install -r requirements/requirements.txt
#COPY . /var/app/
#EXPOSE 8000
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

FROM ubuntu:17.10
WORKDIR /var/app/
RUN apt-get update && apt-get install -y python-pip python-dev git libpq-dev python-virtualenv libjpeg-dev zlib1g-dev build-essential git-core libxslt1-dev
COPY ./requirements /var/app/requirements/
RUN pip install -r requirements/requirements.txt
COPY . /var/app/
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
