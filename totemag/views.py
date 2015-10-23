from django.template.loader import get_template
from django.template import RequestContext
from django.http import HttpResponse


def homepage(request):
    t = get_template('homepage.html')
    html = t.render(RequestContext(request))
    return HttpResponse(html)
