from django.db import models
from ckeditor.fields import RichTextField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Staff(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    image = models.ImageField(
        upload_to='staff')

    featured = models.BooleanField(
        default=False,
        help_text="Show on About page")

    info_text = RichTextField(
        help_text="Text to show under articles for author",
        blank=True)

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
        processors=[ResizeToFill(width=75, height=75)],
        format='JPEG',
        options={'quality': 86})

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        verbose_name_plural = "staff"
