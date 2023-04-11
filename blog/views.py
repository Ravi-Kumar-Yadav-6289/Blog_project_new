from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# consider that after a db call we have a list of dictionaries of the post 
#dummy datasets
# posts=[
#     {
#         'author':'Ravi',
#         'content' : 'First post on this site',
#         'date_posted': "august month post",
#         'title': 'post1'
#     },
#     {
        
#         'author':'modi',
#         'content' : 'Second post on this site',
#         'date_posted': "august month post",
#         'title':'post2'
#     }
# ]


def home(request):
    context={
        'posts':Post.objects.all(),
        'title': "Home"
    }
    return render(request, 'blog/blog_home.html', context)

def about(request):
    context={
        'title': "About"
    }
    return render (request, 'blog/blog_about.html',context)

