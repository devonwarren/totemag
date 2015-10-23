from django.shortcuts import get_object_or_404
from articles.models import Article
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse


def article(request, slug):
    article = get_object_or_404(Article, slug=slug)

    t = get_template('article.html')
    html = t.render(Context({
        'article': article
        }))
    return HttpResponse(html)
