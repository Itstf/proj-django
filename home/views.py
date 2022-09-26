from django.shortcuts import render
from home.models import Post
from home.models import Manchete
from home.models import Welcome

# Create your views here.
def home(request):
    posts = Post.objects.all()
    manchete = Manchete.objects.all()[0]
    manchete2 = Manchete.objects.all()[1]
    welcome = Welcome.objects.all()[0]
    return render(request, 'home.html', {'posts':posts, 'manchete': manchete, 'manchete2': manchete2, 'welcome':welcome})

def post(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'post.html', {'post':post})

def manchete(request, manchete_id):
    manchete = Manchete.objects.get(pk=manchete_id)
    return render(request, 'home.html', {'manchete':manchete})

def welcome(request, welcome_id):
    welcome = Welcome.objects.get(pk=welcome_id)
    return render(request, 'home.html', {'welcome':welcome})