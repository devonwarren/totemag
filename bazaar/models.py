from django.db import models
from ckeditor.fields import RichTextField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Shop(models.Model):
    title = models.CharField(max_length=200)

    image1 = models.ImageField(upload_to='bazaar')
    image2 = models.ImageField(upload_to='bazaar', null=True, blank=True)

    image1_web = ImageSpecField(
        source='image1',
        processors=[ResizeToFill(width=320, height=400)],
        format='JPEG',
        options={'quality': 85})

    image2_web = ImageSpecField(
        source='image2',
        processors=[ResizeToFill(width=320, height=400)],
        format='JPEG',
        options={'quality': 85})

    body = RichTextField()

    submitted = models.DateTimeField(auto_now_add=True)

    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    pinterest = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    tumblr = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)

    def social_media(self):
        return {
            'facebook': self.facebook,
            'twitter': self.twitter,
            'pinterest': self.pinterest,
            'instagram': self.instagram,
            'tumblr': self.tumblr,
            'youtube': self.youtube,
        }

    def __str__(self):
        return self.title
