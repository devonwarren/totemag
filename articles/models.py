from django.db import models
from django.core.cache import cache
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit
from autoslug import AutoSlugField
from staff.models import Staff


def refresh_navigation(**kwargs):
    print("refreshing nav")
    cache.delete('navigation')


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


models.signals.post_save.connect(refresh_navigation)
models.signals.post_delete.connect(refresh_navigation)


class SlideshowImage(models.Model):
    article = models.ForeignKey('Article')

    image = models.ImageField(upload_to='articles')

    image_web = ImageSpecField(
        source='image',
        processors=[ResizeToFit(width=900)],
        format='JPEG',
        options={'quality': 90})

    description = RichTextField()

    def __str__(self):
        return self.description


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

    image = models.ImageField(
        upload_to='articles',
        help_text='Image used on homepage grid, \
        also shown at top of the page unless there are slideshow images')

    image_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(width=275, height=350)],
        format='JPEG',
        options={'quality': 92})

    image_square_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(width=225, height=200)],
        format='JPEG',
        options={'quality': 90})

    image_web = ImageSpecField(
        source='image',
        processors=[ResizeToFit(width=800)],
        format='JPEG',
        options={'quality': 90})

    image_attribution = models.ForeignKey(
        Staff,
        related_name='image_attribution',
        blank=True,
        null=True)

    body = RichTextUploadingField()

    category = models.ForeignKey(
        Category,
        limit_choices_to={'allow_select': True})

    published_date = models.DateField()

    publisher = models.ForeignKey(Staff)

    publish_after = models.DateTimeField(
        null=True, blank=True,
        help_text='If set will be published after this point automatically')

    count = models.IntegerField(
        default=0,
        help_text='Total views')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/article/' + self.slug + '/'

    def is_slideshow(self):
        if (SlideshowImage.objects.filter(article=self.id)):
            return True
        else:
            return False

    def is_tall_image(self):
        """ Returns true if the image is tall instead of wide """
        if ((self.image.height / self.image.width) >= 1.0):
            return True
        else:
            return False

    class Meta:
        ordering = ('-published_date',)
