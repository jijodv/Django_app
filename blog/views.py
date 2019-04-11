from django.shortcuts import render
# Create your views here.

posts = [
    {
        'author': 'Balaji Vellaichamy',
        'title': 'Django - Blog Post 1',
        'content': 'Django - First Post Content',
        'date_posted': 'April 10, 2019'
    },
    {
        'author': 'Aaradhana',
        'title': 'Django - Blog Post 2',
        'content': 'Django - Second Post Content',
        'date_posted': 'April 11, 2019'
    }
]

def home(request):
    context = {
    'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def aara(request):
    return render(request, 'blog/aara.html', {'title': 'Aaradhana'})
