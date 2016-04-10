from django.shortcuts import render, get_object_or_404
from datetime import date
from month.models import Theme, ThemeArticle


def month_view(request, slug=None):
    if slug:
        theme = get_object_or_404(Theme, slug=slug)
    else:
        theme = get_object_or_404(
            Theme,
            month=date.today().month,
            year=date.today().year)

    articles = ThemeArticle.objects.filter(theme=theme).select_related()

    return render(
        request,
        'month.html',
        {
            'theme': theme,
            'articles': articles
        })


def featured_girls(request):
    featured_articles = ThemeArticle.objects.filter(
        article__published=True).order_by('-article__published_date')[:4]
    articles = ThemeArticle.objects.filter(
        article__published=True).order_by('-article__published_date')[4:]

    return render(
        request,
        'featured_girls.html',
        {
            'featured_articles': featured_articles,
            'articles': articles
        })
