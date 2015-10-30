from django.template.loader import get_template
from django.template import RequestContext
from django.http import HttpResponse
from bazaar.models import Shop


def bazaar(request):
    shops = Shop.objects.all().order_by('submitted')
    t = get_template('bazaar.html')
    html = t.render(RequestContext(request, {
            'shops': shops,
        }))
    return HttpResponse(html)
