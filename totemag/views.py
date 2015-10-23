from django.template.loader import get_template
from django.template import RequestContext
from django.http import HttpResponse
from articles.models import Article


def homepage(request):
    articles = Article.objects.all()
    t = get_template('homepage.html')
    html = t.render(RequestContext(request, {
            'articles': articles,
        }))
    return HttpResponse(html)
