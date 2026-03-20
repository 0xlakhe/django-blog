from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.

posts = [
    {
        "author": "Hello",
        "title": "Post 1",
        "content": "First post content",
        "date_posted": "August 41, 1998",
    },
    {
        "author": "Hello2",
        "title": "Post 2",
        "content": "Second post content",
        "date_posted": "November 03, 2000",
    },
]


def home(request):
    context = {"posts": Post.objects.all()}
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {"title": "Hello-about"})


def hello(request):
    return HttpResponse("<h1>Hello</h1>")
