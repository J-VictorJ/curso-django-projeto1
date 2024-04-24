"""
URL configuration for Projeto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import \
    HttpResponse  # method to use the response, return Http...
from django.urls import path


def the_response(request):  # this request is the client's side
    return HttpResponse("Hello, World in this pretty string")  # the response to the client


def another_page(request):  # here it's my home ''
    return HttpResponse("Another page in this 'website' :()")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('sobre/', the_response),
    path('', another_page),
]
