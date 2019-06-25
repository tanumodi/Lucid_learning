from django.shortcuts import render
from django.http import HttpResponse
#from django.contrib.auth.decorators import login_required
from .models import Post

# Create your views he
def welcome(request):
    user = request.user
    try:
    	posts = Post.objects.filter(author = user)
    except:
    	posts= None
    posts
    context = {
        'posts': posts
    }
    return render(request, 'home/welcome.html', context)

def settings(request):
    return render(request, 'home/settings.html')
