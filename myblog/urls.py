"""myblog URL Configuration

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
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = [
	url(r'^$', 'blog.views.index'),
#   url(r'^$', 'rango.views.index'),
    url(r'^rango/', include('rango.urls')),  # ADD THIS NEW TUPLE!
    url(r'^admin/', include(admin.site.urls)),
    url(r'blog/view/(?P<slug>[^\.]+).html', 'blog.views.view_post',name='view_blog_post'),
    url(r'blog/category/(?P<slug>[^/.]+).html', 'blog.views.view_category', name='view_blog_category')
]

# UNDERNEATH your urlpatterns definition, add the following two lines:
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}),)

