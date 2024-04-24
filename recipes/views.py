from django.http import HttpResponse

# from django.shortcuts import render


def home(request):
    return HttpResponse("Hello, World in this pretty string")


def contact(request): 
    return HttpResponse("Another page in this 'website' :()")


def about(request): 
    return HttpResponse("About section")
