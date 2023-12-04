from django.shortcuts import render,get_object_or_404
from .models import *

def blog_view(request,cat_name=None):
    posts=Post.objects.filter(status=1)
    if cat_name:
        posts=posts.filter(category__name=cat_name)
    context={'posts':posts}
    return render(request,'blog/blog-home.html',context)

def single_view(request,pid):
    post=get_object_or_404(Post,pk=pid,status=1)
    context={'post':post}
    return render(request,'blog/blog-single.html',context)

#def cat_view (request,cat_name):
#    posts=Post.objects.filter(status=1)
#    posts=posts.filter(category__name=cat_name)
#    context={'posts':posts}
#    return render(request,'blog/blog-home.html',context)