"""nine URL Configuration

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

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'NineCo.views.Index', name='home'),
    url(r'^About/$', 'NineCo.views.summary', name='About us'),
    url(r'^contact/', 'NineCo.views.contact'),
    url(r'^jobs/', 'NineCo.views.jobs'),
    url(r'^games/', 'NineCo.views.gamelist'),
    url(r'^News', 'NineCo.views.NewsPage', name='news page'),
    url(r'^gameclass/', 'NineCo.views.gamecl'),
    url(r'^game/(\d+)/$', 'NineCo.views.gamed'),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': '/static/'}),
]
