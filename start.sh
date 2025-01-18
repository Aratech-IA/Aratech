#!/usr/bin/env bash
python3 /App/Aratech/manage.py collectstatic --noinput > /App/log_collect_static-$(date +"%Y_%m_%d_%T").log
/App/asgi.sh