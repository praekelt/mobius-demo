FROM praekeltcom/django-bootstrap:latest
COPY . /var/praekelt/app
RUN /var/praekelt/ve/bin/pip install -r /var/praekelt/app/requirements/requirements.txt
RUN /var/praekelt/ve/bin/python /var/praekelt/app/manage.py collectstatic --noinput
VOLUME /mnt/gluster/mobius-demo:/var/praekelt/media
WORKDIR /var/praekelt/app
CMD /root/startProject.sh
