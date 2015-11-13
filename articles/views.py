from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from articles.models import Article, SlideshowImage, Category
from articles.serializers import ArticleSerializer
from rest_framework.renderers import JSONRenderer
from django.template.loader import get_template
from django.template import Context, RequestContext
from django.http import HttpResponse, Http404


ARTICLE_PAGINATION = 16


class JSONResponse(HttpResponse):

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


def list_articles(request, slug=None):
    if slug:
        category = get_object_or_404(Category, slug=slug)
        articles = Article.objects.filter(
            published=True,
            category=category
            ).order_by('-published_date')
    else:
        articles = Article.objects.filter(
            published=True
            ).order_by('-published_date')
        category = None
    paginator = Paginator(articles, ARTICLE_PAGINATION)
    articles = paginator.page(1)

    t = get_template('homepage.html')
    html = t.render(RequestContext(request, {
            'articles': articles,
            'category': category,
            'has_more': articles.has_next(),
        }))
    return HttpResponse(html)


def article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    slideshow_images = SlideshowImage.objects.filter(article=article)

    t = get_template('article_full.html')
    html = t.render(Context({
        'article': article,
        'slideshow': slideshow_images
        }))
    return HttpResponse(html)


def article_html(request, slug):
    article = get_object_or_404(Article, slug=slug)
    slideshow_images = SlideshowImage.objects.filter(article=article)

    t = get_template('article.html')
    html = t.render(Context({
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

        serializer = ArticleSerializer(articles, many=True)
        return JSONResponse(serializer.data)
