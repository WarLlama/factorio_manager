from __future__ import absolute_import

import docker

from celery import shared_task
from django.conf import settings
from containers.models import Container


@shared_task
def fetch_containers():
    client = docker.DockerClient(base_url=settings.DOCKER_SOCKET_URL, version=settings.DOCKER_API_VERSION)
    all_containers = client.containers.list(all=True)
    for c in all_containers:
        new_c = Container.objects.get_or_create(
            id=c.id,
            image=c.attrs['Config']['Image'],
            created=c.attrs['Created'],
            started=c.attrs['State']['StartedAt'],
            status=c.attrs['State']['Status'],
            name=c.attrs['Name'])
        new_c.save()

