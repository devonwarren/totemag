from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class AdImage(models.Model):
    image = models.ImageField(
        upload_to='ads')

    published = models.BooleanField(default=False)

    caption = models.CharField(max_length=120)

    url = models.URLField()

    def __str__(self):
        return self.caption


class TopAdImage(AdImage):
    image_web = ImageSpecField(
        source='image',
        processors=[ResizeToFill(
            width=728,
            height=90)],
        format='JPEG',
        options={'quality': 90})

    class Meta:
        verbose_name_plural = "Top Ads"


class HeaderAdImage(AdImage):
    image_web = ImageSpecField(
        source='image',
        processors=[ResizeToFill(
            width=970,
            height=250)],
        format='JPEG',
        options={'quality': 90})

    class Meta:
        verbose_name_plural = "Header Ads"


class SideAdImage(AdImage):
    image_web = ImageSpecField(
        source='image',
        processors=[ResizeToFill(
            width=300,
            height=600)],
        format='JPEG',
        options={'quality': 90})

    class Meta:
        verbose_name_plural = "Side Ads"
