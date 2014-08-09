#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

git pull origin master

mkdir venv
virtualenv $DIR/venv/ghtopanal
source $DIR/venv/ghtopanal/bin/activate

pip install -r requirements.txt

HOST=`wget -O - -q -T 3 -t 1 http://169.254.169.254/latest/meta-data/public-ipv4`
if [ $? != 0 ]; then
    HOST=`/sbin/ifconfig | sed -n 's/.*inet addr:\([0-9.]\+\)\s.*/\1/p' | tail -1`
fi
PORT=8911

celery -A microhackaton worker -D

PIDFILE='/tmp/ghtopanal.pid'

uwsgi --stop $PIDFILE
uwsgi --chdir=$DIR --module=microhackaton.wsgi:application --env DJANGO_SETTINGS_MODULE=microhackaton.settings --env HOST=$HOST --env PORT=$PORT --http=0.0.0.0:$PORT --home=$DIR/venv/ghtopanal

#--processes=5 --harakiri=20 --max-requests=5000 --vacuum

# --master --pidfile=$PIDFILE --daemonize=$DIR/ghtopanal.log

#