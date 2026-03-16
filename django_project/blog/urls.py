from django.urls import path
from django.http import HttpResponse
from . import views

urlpatterns = [
    path("", views.home, name="blog-home"),
    path("about/", views.about, name="about"),
    path("hello/", views.hello, name="hello"),
]
