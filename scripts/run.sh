#!/bin/bash
set -e
LOGFILE=/var/log/gunicorn/django_app.log
LOGDIR=$(dirname $LOGFILE)
NUM_WORKERS=3
#cd /home/ubuntu/django_app
#source bin/activate
cd /home/ubuntu/deranreger
test -d $LOGDIR || mkdir -p $LOGDIR
exec gunicorn_django -w $NUM_WORKERS \
  --log-level=debug \
  --log-file=$LOGFILE 2>>$LOGFILE
