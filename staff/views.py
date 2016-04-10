from staff.models import Staff
from articles.models import Article
from django.shortcuts import get_object_or_404, render
from django.db.models import Q
from datetime import date, timedelta


def staff_view(request, slug):
    staff = get_object_or_404(Staff, slug=slug)

    articles = Article.objects.filter(
        Q(publisher=staff, published=True) |
        Q(image_attribution=staff, published=True))

    popular_articles = Article.objects.filter(
        Q(
            published=True,
            published_date__gte=(date.today() - timedelta(days=31)),
            publisher=staff.id) |
        Q(
            published=True,
            published_date__gte=(date.today() - timedelta(days=31)),
            image_attribution=staff.id)
        ).order_by('-count')[:6]

    return render(
        request,
        'staff_view.html',
        {
            'staff': staff,
            'articles': articles,
            'popular_articles_side': popular_articles,
        })
