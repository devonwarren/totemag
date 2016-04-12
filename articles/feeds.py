from datetime import datetime, time
from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Rss201rev2Feed
from articles.models import Article


class ToteFeedGenerator(Rss201rev2Feed):
    def add_root_elements(self, handler):
        super(ToteFeedGenerator, self).add_root_elements(handler)
        handler.addQuickElement('webfeeds:analytics', '', {
                'id': 'UA-40610810-1',
                'engine': 'GoogleAnalytics',
            })
        handler.addQuickElement(
            'webfeeds:logo',
            'http://www.totemag.com/static/images/logo/logo.svg')
        handler.addQuickElement('webfeeds:accentColor', '40c0c5')


class LatestEntriesFeed(Feed):
    feed_type = ToteFeedGenerator
    title = "Tote"
    link = "/"
    description = "Latest articles from Tote Mag"

    def items(self):
        return Article.objects.order_by('-published_date')[:25]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body

    def item_author_name(self, item):
        return item.publisher

    def item_pubdate(self, item):
        return datetime.combine(item.published_date, time())
