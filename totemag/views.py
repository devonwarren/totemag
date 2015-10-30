from django.template.loader import get_template
from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from articles.models import Article
from staff.models import Staff
import mailchimp


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


def contact(request):
    if request.method == 'POST':

        to_email = 'comments@totemag.com'
        reason = request.POST.get('reason')

        if reason == 'join':
            to_email = 'contribute@totemag.com'
        elif reason == 'intern':
            to_email = 'intern@totemag.com'
        elif reason == 'feature':
            to_email = 'feature@totemag.com'
        elif reason == 'support':
            to_email = 'support@totemag.com'

        send_mail(
            'Message from ' + request.POST.get('name'),
            request.POST.get('message'),
            request.POST.get('email'),
            [to_email])

        messages.add_message(request, messages.INFO,
            "Thanks for contacting us! We will get back to you shortly!")

        return redirect(request.POST.get('return_url'))
    t = get_template('contact.html')
    html = t.render(RequestContext(request))
    return HttpResponse(html)


def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            api = mailchimp.Mailchimp(settings.MAILCHIMP_API_KEY)
            api.lists.subscribe('0c1c51c413', {'email': email})
            messages.add_message(request, messages.INFO,
                "Thanks for subscribing! You should have a confirmation email.")
        except mailchimp.ListAlreadySubscribedError as detail:
            messages.add_message(request, messages.INFO,
                "You are already subscribed!")
        return redirect('/')
