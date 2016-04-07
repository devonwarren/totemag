from staff.models import Staff
from articles.models import Article
from django.shortcuts import get_object_or_404
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from datetime import date, timedelta


def staff_view(request, slug):
    staff = get_object_or_404(Staff, slug=slug)
    articles = Article.objects.filter(publisher=staff)
    popular_articles = Article.objects.filter(
        published=True,
        published_date__gte=(date.today() - timedelta(days=31)),
        publisher=staff.id
        ).order_by('-count')[:6]

    t = get_template('staff_view.html')
    html = t.render(Context({
        'staff': staff,
        'articles': articles,
        'popular_articles_side': popular_articles,
        }))
    return HttpResponse(html)
