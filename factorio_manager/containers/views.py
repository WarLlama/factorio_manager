from django.http import HttpResponse
import docker

client = docker.from_env()


def index(request):
    running_containers = client.containers.list()
    response = ""
    for container in running_containers:
        response += "id={}|image={}\n".format(container.id, container.image)
    return HttpResponse(response)