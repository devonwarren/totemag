from django.shortcuts import render, get_object_or_404
from datetime import date
from month.models import Theme


def month_view(request, slug=None):
    if slug:
        theme = get_object_or_404(Theme, slug=slug)
    else:
        theme = get_object_or_404(Theme,
            month=date.today().month,
            year=date.today().year)

    return render(
        request,
        'month.html',
        {'theme': theme})
