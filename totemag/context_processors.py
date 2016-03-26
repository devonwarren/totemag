from articles.models import Category
from django.core.cache import cache


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
