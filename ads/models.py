from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from articles.models import Category


SECTIONS = (
        ('1', 'homepage'),
        )


class HeaderAdImage(models.Model):
    image = models.ImageField(
        upload_to='ads')

    image_web = ImageSpecField(
        source='image',
        processors=[ResizeToFill(
            width=970,
            height=250)],
        format='JPEG',
        options={'quality': 90})

    published = models.BooleanField(default=False)

    caption = models.CharField(max_length=120, blank=True, null=True)

    url = models.URLField()

    #categories = models.ManyToManyField(Category)

    #sections = models.CharField(
    #    max_length=4,
    #    choices=SECTIONS,
    #    null=True)

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name_plural = "Header Ads"


class SideAdImage(models.Model):
    image = models.ImageField(
        upload_to='ads')

    image_web = ImageSpecField(
        source='image',
        processors=[ResizeToFill(
            width=300,
            height=600)],
        format='JPEG',
        options={'quality': 90})

    published = models.BooleanField(default=False)

    caption = models.CharField(max_length=120, blank=True, null=True)

    url = models.URLField()

    #categories = models.ManyToManyField(Category)

    #sections = models.CharField(
    #    max_length=4,
    #    choices=SECTIONS,
    #    null=True)

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name_plural = "Side Ads"
