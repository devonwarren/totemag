from haystack import indexes
from articles.models import Article


class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    author = indexes.CharField(model_attr='publisher')
    title = indexes.CharField(model_attr='title')
    body = indexes.CharField(model_attr='body')
    category = indexes.CharField(model_attr='category')
    pub_date = indexes.DateTimeField(model_attr='published_date')

    def get_model(self):
        return Article

    def index_queryset(self, using=None):
        return self.get_model().objects.filter(published=True)
