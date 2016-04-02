from django.core.management.base import BaseCommand
from django.utils import timezone
from articles.models import Article


class Command(BaseCommand):
    help = 'Publishes articles automatically'

    def handle(self, *args, **options):
        articles = Article.objects.filter(
            published=False,
            publish_after__lte=timezone.now())

        for article in articles:
            article.published = True
            article.published_date = timezone.now()
            article.save(update_fields=['published', 'published_date'])
            self.stdout.write(self.style.SUCCESS(
                'Published article "%s"' % article.title))
