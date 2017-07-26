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
        new_c = Container.objects.get_or_create(id=c.id)
        new_c.image=c.attrs['Config']['Image']
        new_c.created = c.attrs['Created']
        new_c.started = c.attrs['State']['StartedAt']
        new_c.status = c.attrs['State']['Status']
        new_c.name = c.attrs['Name']
        new_c.save()

