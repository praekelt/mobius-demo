FROM cloud.canister.io:5000/praekeltconsulting/django-bootstrap:latest
COPY . /var/praekelt/app
RUN chown -R praekelt: /var/praekelt
RUN runuser -l praekelt -c '/var/praekelt/ve/bin/pip install -r /var/praekelt/app/requirements/requirements.txt'
RUN runuser -l praekelt -c '/var/praekelt/ve/bin/python /var/praekelt/app/manage.py collectstatic --noinput'
EXPOSE 8080
VOLUME /mnt/gluster/mobius-demo:/var/praekelt/media
WORKDIR /var/praekelt/app
CMD /root/startProject.sh
