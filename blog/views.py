from django.shortcuts import render
from django.http import HttpResponse

# consider that after a db call we have a list of dictionaries of the post 

posts=[
    {
        'author':'Ravi',
        'content' : 'First post on this site',
        'date': "august month post"
    },
    {
        
        'author':'modi',
        'content' : 'Second post on this site',
        'date': "august month post"
    }
]


def home(request):
    context={
        'posts':posts,
        'title': "Home"
    }
    return render(request, 'blog/blog_home.html', context)

def about(request):
    context={
        'title': "About"
    }
    return render (request, 'blog/blog_about.html',context)

