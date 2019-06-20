from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def welcome(request):
    user = request.user
    posts = Post.objects.get(author = user)
    posts
    context = {
        'posts': posts
    }
    return render(request, 'home/welcome.html', context)

def settings(request):
    return render(request, 'home/settings.html')
