from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.syndication.views import Feed
from articles.models import Article, SlideshowImage, Category
from rest_framework.renderers import JSONRenderer
from django.template.loader import get_template, render_to_string
from django.template import RequestContext
from django.http import HttpResponse, Http404
from datetime import date, timedelta, datetime, time


ARTICLE_PAGINATION = 20


class JSONResponse(HttpResponse):

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


class LatestEntriesFeed(Feed):
    title = "Totemag.com"
    link = "/"
    description = "Latest articles from Tote"

    def items(self):
        return Article.objects.order_by('-published_date')[:25]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body

    def item_author_name(self, item):
        return item.publisher.name

    def item_pubdate(self, item):
        return datetime.combine(item.published_date, time())


def list_articles(request, slug=None):
    if slug:
        category = get_object_or_404(Category, slug=slug)
        featured_articles = Article.objects.filter(
            published=True,
            category=category
            ).order_by('-published_date')[:4]
        articles = Article.objects.filter(
            published=True,
            category=category
            ).order_by('-published_date')[4:20]
        popular_articles = Article.objects.filter(
            published=True,
            published_date__gte=(date.today() - timedelta(days=31)),
            category=category
            ).order_by('-count')[:6]
    else:
        featured_articles = Article.objects.filter(
            published=True
            ).order_by('-published_date')[:4]
        articles = Article.objects.filter(
            published=True
            ).order_by('-published_date')[4:20]
        category = None
        popular_articles = None

    shown_subscribe = False
    if request.session.get('shown_subscribe', False):
        shown_subscribe = True
    else:
        request.session['shown_subscribe'] = True

    t = get_template('homepage.html')
    html = t.render(RequestContext(request, {
            'featured_articles': featured_articles,
            'recent_articles': articles,
            'category': category,
            'popular_articles_side': popular_articles,
            'shown_subscribe': shown_subscribe,
        }))
    return HttpResponse(html)


def article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    slideshow_images = SlideshowImage.objects.filter(article=article)

    article.count += 1
    article.save(update_fields=["count"])

    t = get_template('article.html')
    html = t.render(RequestContext(request, {
        'article': article,
        'slideshow': slideshow_images
        }))
    return HttpResponse(html)


def api_article_list(request, page=1, category=None):
    if request.method == 'GET':

        if category:
            cat = get_object_or_404(Category, slug=category)
            article_list = Article.objects.filter(
                published=True,
                category=cat)
        else:
            article_list = Article.objects.filter(published=True)

        paginator = Paginator(article_list, ARTICLE_PAGINATION)
        try:
            articles = paginator.page(page)
        except PageNotAnInteger:
            articles = paginator.page(1)
        except EmptyPage:
            raise Http404('No more articles on page ' + page)

        html = ''
        for article in articles:
            html += render_to_string('article_teaser.html', {
                    'article': article,
                })

        return HttpResponse(html)
