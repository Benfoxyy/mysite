from django import template
from blog.models import Post,category
register=template.Library()

@register.simple_tag(name='count')
def count():
    posts = Post.objects.filter(status=True).count()
    return posts

@register.simple_tag(name='show')
def show():
    posts = Post.objects.filter(status=True)
    return posts

@register.filter
def summarize(value,arg):
    return value[:arg] + ' ...'

@register.inclusion_tag('blog/latest_posts.html')
def latest_posts(arg=3):
    posts=Post.objects.filter(status=True).order_by('-published_date')[:arg]
    return {'posts': posts}


@register.inclusion_tag('blog/post_categories.html')
def postcategories():
    posts=Post.objects.filter(status=True)
    categories=category.objects.all()
    cat_dict={}
    for name in categories:
        cat_dict[name]=posts.filter(category=name).count()
    return {'categories': cat_dict}