# uvicorn is good for light application with --reload
uvicorn --ws auto  --host 0.0.0.0 --port 9090 --reload Aratech.asgi:application

# gunicorn is suitable for production with process management
#gunicorn  -b 0.0.0.0:9090 -w 4 -k uvicorn.workers.UvicornWorker projet.asgi:application