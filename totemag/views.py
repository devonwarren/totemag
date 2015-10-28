from django.template.loader import get_template
from django.template import RequestContext
from django.http import HttpResponse
from articles.models import Article
from staff.models import Staff


def homepage(request):
    articles = Article.objects.all()
    t = get_template('homepage.html')
    html = t.render(RequestContext(request, {
            'articles': articles,
        }))
    return HttpResponse(html)


def about(request):
    staff = Staff.objects.all()
    t = get_template('about.html')
    html = t.render(RequestContext(request, {
            'staff': staff,
        }))
    return HttpResponse(html)


def videos(request):
    t = get_template('videos.html')
    html = t.render(RequestContext(request))
    return HttpResponse(html)
