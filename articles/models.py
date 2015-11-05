from django.db import models
from ckeditor.fields import RichTextField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit
from autoslug import AutoSlugField
from staff.models import Staff
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField(max_length=100)

    slug = AutoSlugField(
        populate_from='name',
        editable=False,
        always_update=True,
        unique=True,
        null=True,
        verbose_name='URL')

    allow_select = models.BooleanField(
        default=True, help_text='Allow articles to be added to this category')

    parent = models.ForeignKey(
        "self", null=True, blank=True,
        related_name='children')

    def __str__(self):
        if self.parent:
            return self.parent.name + " > " + self.name
        else:
            return self.name

    class Meta:
        verbose_name_plural = "categories"


#@python_2_unicode_compatible
#class SlideshowImage(models.Model):
#    image = models.ImageField(upload_to='articles')

#    image_web = ImageSpecField(
#        source='image',
#        processors=[ResizeToFit(width=900)],
#        format='JPEG',
#        options={'quality': 76})
#
#    description = models.CharField(max_length=250)


@python_2_unicode_compatible
class Article(models.Model):
    title = models.CharField(max_length=200)

    published = models.BooleanField(
        default=False,
        help_text='Allow the public to see the page')

    slug = AutoSlugField(
        populate_from='title',
        editable=False,
        always_update=True,
        unique=True,
        null=True,
        verbose_name='URL',
        help_text='URL for page details (\'/article/URL\')')

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

    #slideshow_images = models.ManyToManyField(
    #    SlideshowImage, through='ArticleSlideshowImage')

    category = models.ForeignKey(
        Category,
        limit_choices_to={'allow_select': True})

    published_date = models.DateField()

    publisher = models.ForeignKey(Staff)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/article/' + self.slug + '/'


#@python_2_unicode_compatible
#class ArticleSlideshowImage(models.Model):
#    article = models.ForeignKey(Article)
#    slideshow = models.ForeignKey(SlideshowImage)
