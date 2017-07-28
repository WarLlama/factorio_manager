from __future__ import absolute_import

import docker

from celery import shared_task
from django.conf import settings
from containers.models import Container

client = docker.DockerClient(base_url=settings.DOCKER_SOCKET_URL, version=settings.DOCKER_API_VERSION)

ports = {
    '34197/udp': '34197',
    '27015/tcp': '27015',
}
@shared_task
def fetch_containers():
    all_containers = client.containers.list(all=True)
    for c in all_containers:
        container, created = Container.objects.update_or_create(
            id=c.id,
            image=c.attrs['Config']['Image'],
            created=c.attrs['Created'],
            started=c.attrs['State']['StartedAt'],
            status=c.attrs['State']['Status'],
            name=c.attrs['Name'])

@shared_task
def start_container(tag, name):
    image = 'dtandersen/factorio:{}'.format(tag)
    client.images.pull('dtandersen/factorio', tag=tag)
    client.containers.run(
        image,
        name=name,
        detach=True,
        devices=['/tmp/factorio:/factorio'],
        ports=ports,
        restart_policy={'Name': 'always'})
