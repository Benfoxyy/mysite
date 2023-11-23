from django.urls import path
from blog.views import *

app_name='blog'

urlpatterns = [
    path('',blog_view,name='home'),
    path('single',single_view,name='single'),
    path('test',test,name='test'),
]