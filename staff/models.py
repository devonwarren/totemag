from django.db import models
from ckeditor.fields import RichTextField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from autoslug import AutoSlugField


class Staff(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)

    slug = AutoSlugField(
        populate_from='name',
        editable=False,
        always_update=True,
        unique=True,
        null=True)

    image = models.ImageField(
        upload_to='staff')

    featured = models.BooleanField(
        default=False,
        help_text="Show on About page")

    info_text = RichTextField(
        help_text="Text to show under articles for author",
        blank=True)

    description = RichTextField()

    image_web = ImageSpecField(
        source='image',
        processors=[ResizeToFill(width=500, height=500)],
        format='JPEG',
        options={'quality': 85})

    image_small = ImageSpecField(
        source='image',
        processors=[ResizeToFill(width=225, height=200)],
        format='JPEG',
        options={'quality': 85})

    image_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(width=75, height=75)],
        format='JPEG',
        options={'quality': 86})

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

    def name(self):
        return self.__str__()

    def __str__(self):
        return self.first_name + " " + self.last_name

    def get_absolute_url(self):
        return '/staff/' + str(self.slug) + '/'

    class Meta:
        verbose_name_plural = "staff"
