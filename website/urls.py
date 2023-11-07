from django.urls import path
from website.views import *

urlpatterns = [
    path('',home_view),
    path('about_us',about_view),
]