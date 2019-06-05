#author angel quingaluisa
# archivo que levanta el app server del microservicio

#!/bin/bash

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn devops_env.wsgi:application --bind 0.0.0.0:8001 --workers 3