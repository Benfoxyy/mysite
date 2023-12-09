from django.urls import path
from .views import *

app_name='website'

urlpatterns = [
    path('',index_view,name='home'),
    path('about',about_view,name='about'),
    path('contact',contact_view,name='contact'),
    path('newsletter',news_view,name='newsletter'),
]