from django.db import models
from ckeditor.fields import RichTextField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToCover
from autoslug import AutoSlugField
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=200)

    slug = AutoSlugField(
        populate_from='title',
        editable=False,
        always_update=True,
        unique=True,
        null=True)

    image = models.ImageField(upload_to='journal')

    image_web = ImageSpecField(
        source='image',
        processors=[ResizeToCover(width=225, height=200)],
        format='JPEG',
        options={'quality': 78})

    body = RichTextField()

    published_date = models.DateField()

    publisher = models.ForeignKey(User)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/article/' + self.slug + '/'
