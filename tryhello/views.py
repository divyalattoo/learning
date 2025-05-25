from django.http import HttpResponse


def hello_world(request,name):
    return HttpResponse("Hello " + name)

