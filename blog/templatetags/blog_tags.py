from django import template
from blog.models import Post
register=template.Library()

@register.simple_tag(name='count')
def funcsion():
    posts = Post.objects.filter(status=True).count()
    return posts

@register.simple_tag(name='show')
def funcsion():
    posts = Post.objects.filter(status=True)
    return posts

@register.filter
def summarize(value,arg):
    return value[:arg] + ' ...'