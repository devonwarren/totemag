from django.db import models
from ckeditor.fields import RichTextField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Staff(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='staff')
    description = RichTextField()

    image_full = ImageSpecField(
        source='image',
        processors=[ResizeToFill(width=500, height=500)],
        format='JPEG',
        options={'quality': 80})

    image_small = ImageSpecField(
        source='image',
        processors=[ResizeToFill(width=225, height=200)],
        format='JPEG',
        options={'quality': 75})

    image_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(width=140, height=140)],
        format='JPEG',
        options={'quality': 75})

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        verbose_name_plural = "staff"
