#!/bin/bash

/etc/init.d/rabbitmq-server start
/etc/init.d/redis-server start
/etc/init.d/memcached start
/etc/init.d/varnish start
/etc/init.d/nginx start
/usr/bin/supervisord -n -c /etc/supervisor/supervisord.conf
