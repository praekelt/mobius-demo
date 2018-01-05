#!/bin/bash

/etc/init.d/rabbitmq-server start
/etc/init.d/redis-server start
/etc/init.d/memcached start
/etc/init.d/supervisor start
/etc/init.d/varnish start
/etc/init.d/nginx start
python manage.py runserver 0.0.0.0:8000
