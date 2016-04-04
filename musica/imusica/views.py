from django.shortcuts import HttpResponse


def mainpage(request):
    return HttpResponse("Hola!")
