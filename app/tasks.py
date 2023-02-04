from subprocess import run
from celery import shared_task
from app.models import App, AppStatus
import shutil
from app.docker_control import *

client = docker.from_env()


@shared_task
def create_container(id_app):
    with open(f'app/docker_task/{id_app}/Dockerfile', 'w') as file:
        text = 'FROM python:3-alpine\n\n' \
 \
               'WORKDIR /app\n\n' \
 \
               f'COPY {id_app}.zip .\n\n' \
 \
               f'RUN  apt-get update; apt install unzip; unzip {id_app}.zip; rm {id_app}.zip; ' \
               'echo >> requirements.txt; pip install --no-cache-dir -r requirements.txt;\n\n' \
 \
               'CMD ["python", "main.py"]'

        file.write(text)
    docker_command = f'docker build app/docker_task/{id_app}/. -t {id_app}'
    run(docker_command.split())
    run(f'docker run --name {id_app} -d {id_app}'.split())
    app = App.objects.get(pk=id_app)
    status = AppStatus.objects.get(pk=get_status(id_app))
    app.app_status = status
    app.docker_id = client.containers.get(str(id_app)).short_id
    app.save()

    shutil.rmtree(f'app/docker_task/{id_app}')

    return f'Container {id_app} created'


@shared_task
def start_container(id_app):
    container = start_app(id_app)
    return f'Container {container.name} started'


@shared_task
def stop_container(id_app):
    container = stop_app(id_app)
    return f'Container {container.name} stopped'


@shared_task
def restart_container(id_app):
    container = restart_app(id_app)

    app = App.objects.get(pk=id_app)
    app.app_status = AppStatus.objects.get(pk=2)
    app.save()
    return f'Container {container.name} restarted'


@shared_task
def delete_container(id_app):
    delete_app(id_app)
    return f'Container {id_app} delited'


@shared_task
def update_status_container():
    apps = App.objects.all()
    for app in apps:
        id_status = get_status(app.docker_id)

        if id_status == -1:
            id_status = 3

        app.app_status = AppStatus.objects.get(pk=id_status)
        app.save()