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
from django.views.generic import TemplateView

from totemag.views import homepage, about, videos, \
    contact, advertise, subscribe
from articles.views import article, list_articles, \
    api_article_list
from bazaar.views import bazaar
from staff.views import staff_view
from month.views import month_view, featured_girls

from django.contrib import admin
admin.autodiscover()


urlpatterns = [
    url(r'^$', homepage, name='homepage'),
    url(r'^about/$', about, name='about'),
    url(r'^month/$', month_view, name='month'),
    url(r'^videos/$', videos, name='videos'),
    url(r'^contact/$', contact, name='contact'),
    url(r'^advertise/$', advertise, name='advertise'),
    url(r'^terms/$',
        TemplateView.as_view(template_name='terms.html'),
        name='terms'),
    url(r'^bazaar/$', bazaar, name='bazaar'),
    url(r'^subscribe/$', subscribe, name='subscribe'),
    url(r'^article/(?P<slug>.+?)/$', article),
    url(r'^staff/(?P<slug>.+?)/$', staff_view),
    url(r'^month/(?P<slug>.+?)/$', month_view),
    url(r'^featured-girls/$', featured_girls),
    url(r'^list/(?P<slug>.+?)/$', list_articles),
    url(r'^search/', include('haystack.urls')),
    url(r'^api/article_list/(?P<category>.+?)/(?P<page>[0-9]+)/$',
        api_article_list),
    url(r'^api/article_list/(?P<page>[0-9]+)/$', api_article_list),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^admin/', include(admin.site.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
