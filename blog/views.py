from urllib import request
from django.shortcuts import render
from matplotlib.style import context
from .models import Post


posts = [
    {
        'author' : 'Hanish',
        'title' : 'Song of Achilles',
        'content' : 'First Post',
        'date_posted' : 'June 30 2022'
    },

    {
        'author' : 'Desiree',
        'title' : 'Vanishing Half',
        'content' : 'Second Post',
        'date_posted' : 'June 30 2023'
    }
]


def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title' : 'About'})
 