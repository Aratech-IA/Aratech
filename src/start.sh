#!/usr/bin/env bash
python /App/manage.py collectstatic --noinput > /App/log_collect_static-$(date +"%Y_%m_%d_%T").log
python /App/manage.py migrate > /App/log_migrate-$(date +"%Y_%m_%d_%T").log
/App/asgi.sh