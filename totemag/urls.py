"""totemag URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static

from totemag.views import homepage, about, videos, contact, subscribe
from articles.views import article

from django.contrib import admin
admin.autodiscover()


urlpatterns = [
    url(r'^$', homepage, name='homepage'),
    url(r'^about/$', about, name='about'),
    url(r'^videos/$', videos, name='videos'),
    url(r'^contact/$', contact, name='contact'),
    url(r'^subscribe/$', subscribe, name='subscribe'),
    url(r'^article/(?P<slug>.+?)/$', article),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
