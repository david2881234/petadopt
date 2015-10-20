"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from pets_adopt import views
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','pets_adopt.views.index', name='index'),
    url(r'^signup/$','pets_adopt.views.user_signup', name='signup'),
    url(r'^logout/$','pets_adopt.views.user_logout', name='logout'),
    url(r'^login/$','pets_adopt.views.user_login',name='login'),
    url(r'^post/new/$','pets_adopt.views.new_pet',name='new_pets'),
    url(r'^post/detail/(?P<pets_id>\d+)/$','pets_adopt.views.pet_detail',name='pet_detail'),
    url(r'^post/adopt/(?P<pets_id>\d+)/$','pets_adopt.views.pet_adopt',name='pet_adopt'),
    url(r'^post/adopt/success/(?P<adopt_id>\d+)/$','pets_adopt.views.pet_adopt_success',name='pet_adopt_success'),
]
