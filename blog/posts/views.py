from django.shortcuts import redirect, render
from django.http import HttpResponse

from .forms import PostForm


def create(request):
    if request.method == "POST": 
        form = PostForm(request.POST)
        # if form.is_valid():
        print("Hi there:")
        print("FOrm:", form)
        form.save(commit=False)
        return redirect("/")
        # else:
        #     print("Error:")
            
    else:
        form = PostForm()
    return render(request, "posts/new.html", {"form": form})
