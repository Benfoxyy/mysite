from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from .models import *
def blog_view(request,cat_name=None,author_username=None,tag_name=None,):
    posts=Post.objects.filter(status=1)
    if cat_name:
        posts=posts.filter(category__name=cat_name)
    if author_username:
        posts=posts.filter(auth__username=author_username)
    if tag_name:
        posts=posts.filter(tags__name__in=[tag_name])
    posts=Paginator(posts,3)
    try:
        page_number=request.GET.get('page')
        posts=posts.get_page(page_number)
    except PageNotAnInteger:
        posts=posts.get_page(1)
    except EmptyPage:
        posts=posts.get_page(1)
    context={'posts':posts}
    return render(request,'blog/blog-home.html',context)

def single_view(request,pid):
    post=get_object_or_404(Post,pk=pid,status=1)
    if post:
        post.counted_views = post.counted_views + 1
        post.save()
    context={'post':post}
    return render(request,'blog/blog-single.html',context)
#def cat_view (request,cat_name):
#    posts=Post.objects.filter(status=1)
#    posts=posts.filter(category__name=cat_name)
#    context={'posts':posts}
#    return render(request,'blog/blog-home.html',context)

def search_view(request):
    posts=Post.objects.filter(status=1)
    if request.method == 'GET':
        if s:= request.GET.get('s'):
            posts=posts.filter(content__contains=s)
    context={'posts': posts}
    return render(request, 'blog/blog-home.html',context)