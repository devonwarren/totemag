from django.core.cache import cache
from django.template.loader import render_to_string
from datetime import date, timedelta
from articles.models import Category, Article
from month.models import Theme, ThemeArticle


def navigation(request):
    if not cache.get('navigation'):
        categories = Category.objects.filter(parent=None).select_related()
        nav = []

        for cat in categories:
            temp = {
                'name': cat.name,
                'slug': cat.slug,
                'children': []
            }
            child = cat.children.all()

            if child:
                for c in child:
                    temp['children'].append({
                            'name': c.name,
                            'slug': c.slug
                        })

            nav.append(temp)

        cache.set('navigation', nav)

    return {
        'navigation': cache.get('navigation'),
    }


def popular_articles(request):
    popular_articles = Article.objects.filter(published=True, 
        published_date__gte=(date.today() - timedelta(days=31))).order_by('-count')[:4]

    html = render_to_string(
        'popular_articles.html',
        {'articles': popular_articles})

    return {
        'popular_articles': html
    }


def month_articles(request):
    theme = Theme.objects.current_theme()
    if theme:
        articles = Theme.objects.current_articles()

        html = render_to_string(
            'month_articles.html',
            {
                'theme': theme,
                'articles': articles
            })
    else:
        html = ''

    return {
        'month_articles': html
    }
