from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from users.models import Profile

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

def profile_page(request):
	curruser= request.user
	posts = Post.objects.filter(author = curruser)
	profile_info= Profile.objects.filter(user= curruser)
	context = {
		'profile_info': profile_info,
		'posts': posts
	}
	return render(request, 'home/profile.html', context)
