from django.urls import path
from blog.views import *

app_name='blog'

urlpatterns = [
    path('',blog_view,name='home'),
    path('post/<int:pid>',single_view,name='single'),
    path('category/<str:cat_name>',blog_view,name='category'),
    path('auth/<str:author_username>',blog_view,name='author'),
    path('search/',search_view,name='search'),
]