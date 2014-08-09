#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

git pull origin master

mkdir venv
virtualenv $DIR/venv/ghtopanal
chmod +x $DIR/venv/ghtopanal/bin/activate
. $DIR/venv/ghtopanal/bin/activate

pip install -r requirements.txt

HOST=`wget -O - -q -T 3 -t 1 http://169.254.169.254/latest/meta-data/public-ipv4`
if [ $? != 0 ]; then
    HOST=`/sbin/ifconfig | sed -n 's/.*inet addr:\([0-9.]\+\)\s.*/\1/p' | tail -1`
fi
PORT=8911

python manage.py runserver $HOST:$PORT
