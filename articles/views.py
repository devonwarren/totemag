from django.shortcuts import get_object_or_404
from articles.models import Article, Category
from django.template.loader import get_template
from django.template import Context, RequestContext
from django.http import HttpResponse


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
    categories = Category.objects.filter(parent=None)
    t = get_template('homepage.html')
    html = t.render(RequestContext(request, {
            'articles': articles,
            'categories': categories,
        }))
    return HttpResponse(html)


def article(request, slug):
    article = get_object_or_404(Article, slug=slug)

    t = get_template('article.html')
    html = t.render(Context({
        'article': article
        }))
    return HttpResponse(html)
