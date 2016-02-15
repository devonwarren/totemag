from articles.models import Category
from totemag.forms import BasicSearchForm


def categories(request):
    all_categories = Category.objects.all()

    return {
        'categories': all_categories,
    }


def search(request):
    return {
        'search_form': BasicSearchForm(load_all=True),
    }
