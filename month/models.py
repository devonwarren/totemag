from django.db import models
from datetime import date
from autoslug import AutoSlugField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from articles.models import Article


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


class ThemeManager(models.Manager):
    def current_theme(self):
        theme = self.get(month=date.today().month, year=date.today().year)
        if theme:
            return theme
        else:
            return None

    def current_articles(self):
        theme = self.current_theme()
        return ThemeArticle.objects.filter(theme=theme)


class Theme(models.Model):
    title = models.CharField(max_length=200)

    slug = AutoSlugField(
        populate_from='name',
        editable=False,
        always_update=True,
        unique=True,
        null=True,
        verbose_name='URL')

    image = models.ImageField(
        upload_to='themes',
        help_text='Image of the header background')

    image_web = ImageSpecField(
        source='image',
        processors=[ResizeToFill(width=800, height=100)],
        format='JPEG',
        options={'quality': 90})

    month = models.IntegerField(choices=MONTHS)

    year = models.IntegerField(choices=year_choices())

    objects = ThemeManager()

    def name(self):
        return str(MONTHS[self.month - 1][1]) + ' ' + str(self.title)

    def month_name(self):
        return str(MONTHS[self.month - 1][1])

    def __str__(self):
        return self.name() + ' (' + str(self.year) + ')'


class ThemeArticle(models.Model):
    theme = models.ForeignKey(Theme, related_name='theme')

    article = models.ForeignKey(Article, related_name='article')

    def __str__(self):
        return self.article.title
