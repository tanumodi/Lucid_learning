from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def welcome(request):
    curruser = request.user
    posts = Post.objects.filter(author = curruser)
    # posts
    context = {
        'posts': posts
    }
    return render(request, 'home/welcome.html', context)

def settings(request):
    return render(request, 'home/settings.html')
