#!/usr/bin/env bash
# gunicorn -b 127.0.0.1:8990 gunicornserver:app --reload
# FLASK_APP=runserver.py:make_app FLASK_ENV=development FLASK_DEBUG=1 python -m flask run
httperf --server 127.0.0.1  --uri /asyn/concurrent  --hog  --num-conns=10000  --port=8990
