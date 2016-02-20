from django.shortcuts import render
from staff.models import Staff
from articles.models import Article
from django.shortcuts import get_object_or_404
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse


def staff_view(request, slug):
    staff = get_object_or_404(Staff, slug=slug)
    articles = Article.objects.filter(publisher=staff)

    t = get_template('staff_view.html')
    html = t.render(Context({
        'staff': staff,
        'articles': articles,
        }))
    return HttpResponse(html)
