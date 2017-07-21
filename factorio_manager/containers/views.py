from django.http import HttpResponse
from django.conf import settings
import docker

client = docker.from_env(version=settings.DOCKER_API_VERSION)


def index(request):
    running_containers = client.containers.list()
    response = ""
    for container in running_containers:
        response += "id={}|image={}\n".format(container.id, container.image)
    return HttpResponse(response)
