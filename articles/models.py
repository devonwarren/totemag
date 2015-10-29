from django.db import models
from ckeditor.fields import RichTextField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit
from autoslug import AutoSlugField
from staff.models import Staff


class Article(models.Model):
    title = models.CharField(max_length=200)

    slug = AutoSlugField(
        populate_from='title',
        editable=True,
        always_update=True,
        unique=True,
        null=True)

    image = models.ImageField(upload_to='articles')

    image_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(width=225, height=200)],
        format='JPEG',
        options={'quality': 76})

    image_web = ImageSpecField(
        source='image',
        processors=[ResizeToFit(width=900)],
        format='JPEG',
        options={'quality': 76})

    image_attribution = models.ForeignKey(
        Staff,
        related_name='image_attribution',
        blank=True,
        null=True)

    body = RichTextField()

    published_date = models.DateField()

    publisher = models.ForeignKey(Staff)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/article/' + self.slug + '/'
