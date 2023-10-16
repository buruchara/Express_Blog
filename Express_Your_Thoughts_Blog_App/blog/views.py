from django.shortcuts import render

posts = [
    {
        'author': 'MikeB',
        'title': 'Blog Post',
        'content': 'First post content',
        'date_posted': 'October 10, 2023'
    },

    {
        'author': 'MIB',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'October 10, 2023'
    }
]


def Home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def About(request):
    return render(request, 'blog/About.html', {'title': 'About'})