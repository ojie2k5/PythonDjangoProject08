from django.shortcuts import render
from .models import Post
# Create your views here.

# List (dictionary)
# posts = [
    #{
    #    'author': 'CoreyMS',
    #    'title': 'Blog Post 1',
    #    'content': 'First post content 1',
    #    'date_posted': 'August 27,2021',
    #},
    #{
    #    'author': 'Jane Doe',
    #    'title': 'Blog Post 2',
    #    'content': 'First post content 2',
    #    'date_posted': 'August 28,2021',
   # },
# ]


def home(request):
    # add a dictionary example:  context = {"key", "value'}
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About', })