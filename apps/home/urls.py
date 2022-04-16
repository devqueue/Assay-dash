# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views
from django.urls import path, include

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('lab1/', include('apps.lab1.urls')),
    path('lab2/', include('apps.lab2.urls')),
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

] 
