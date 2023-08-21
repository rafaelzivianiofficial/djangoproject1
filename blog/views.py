from django.shortcuts import render
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})




















"""posts = [
    {
        'author': 'Rafael Ziviani',
        'title': 'Python 101',
        'content': 'Learning Django',
        'date_posted': 'April 04, 2023',
    },
    {
        'author': 'Rafael',
        'title': 'Django is awesome',
        'content': 'Learning A LOT',
        'date_posted': 'December 2023',
    },
]"""