# Biohack 

# docker-flask-gunicorn-nginx

Bootstrap example of a Flask/Dash app served via Gunicorn and Nginx using Docker containers
Guildeline article can be found at https://sladkovm.github.io/webdev/2017/10/16/Deploying-Plotly-Dash-in-a-Docker-Container-on-Digitital-Ocean.html

### Run

```bash
/bin/bash run_docker.sh
```


```bash
echo killing old docker processes
docker-compose rm -fs

echo building docker containers
docker-compose up --build -d
```

1. It will kill all running docker processes.
2. Will start all required containers in background

