from django.shortcuts import render
from django.http import HttpResponse

from posts.models import Post

def welcome(request):
    return render(
        request, 
        "website/welcome.html",
        {
            "posts": Post.objects.all(),
            "count":Post.objects.count()
        }
     )
