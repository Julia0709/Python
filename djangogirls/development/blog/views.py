from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    # parse request
    # access databese
    # get data
    # sending it back...

    # get all my posts from the database.
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def about(request):
    return render(request, 'blog/about.html')
