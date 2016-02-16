from django.db import models
from datetime import date


MONTHS = (
    (1, 'January'),
    (2, 'February'),
    (3, 'March'),
    (4, 'April'),
    (5, 'May'),
    (6, 'June'),
    (7, 'July'),
    (8, 'August'),
    (9, 'September'),
    (10, 'October'),
    (11, 'November'),
    (12, 'December'),
)


def year_choices():
    years = []
    for y in range(2015, date.today().year + 2):
        years.append((y, y))
    return years


class Theme(models.Model):
    title = models.CharField(max_length=200)

    image = models.ImageField(
        upload_to='themes',
        help_text='Image of the header background')

    month = models.IntegerField(
        max_length=2,
        choices=MONTHS)

    year = models.IntegerField(
        max_length=4,
        choices=year_choices())

    def name(self):
        return str(MONTHS[self.month - 1][1]) + ' ' + str(self.title)

    def __str__(self):
        return self.name() + ' (' + str(self.year) + ')'
