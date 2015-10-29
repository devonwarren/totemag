from django.template.loader import get_template
from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import redirect
from articles.models import Article
from staff.models import Staff
from django.conf import settings
import mailchimp
from django.contrib import messages


def homepage(request):
    articles = Article.objects.all()
    t = get_template('homepage.html')
    html = t.render(RequestContext(request, {
            'articles': articles,
        }))
    return HttpResponse(html)


def about(request):
    staff = Staff.objects.filter(featured=True)
    t = get_template('about.html')
    html = t.render(RequestContext(request, {
            'staff': staff,
        }))
    return HttpResponse(html)


def videos(request):
    t = get_template('videos.html')
    html = t.render(RequestContext(request))
    return HttpResponse(html)


def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            api = mailchimp.Mailchimp(settings.MAILCHIMP_API_KEY)
            api.lists.subscribe('770a3ce5b5', {'email': email})
            messages.add_message(request, messages.INFO,
                "Thanks for subscribing! You should have a confirmation email.")
        except mailchimp.ListAlreadySubscribedError as detail:
            messages.add_message(request, messages.INFO,
                "You are already subscribed!")
        return redirect('/')
