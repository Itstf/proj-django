from django.shortcuts import render
from home.models import Post
from home.models import Manchete

# Create your views here.
def home(request):
    posts = Post.objects.all()
    manchetes = Post.objects.all()
    return render(request, 'home.html', {'posts':posts})

def post(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'post.html', {'post':post})

def manchete(request, manchete_id):
    manchete = Manchete.objects.get(pk=manchete_id)
    return render(request, 'home.html', {'manchete':manchete})