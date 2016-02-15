from haystack import indexes
from staff.models import Staff


class StaffIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    title = indexes.CharField(model_attr='title')
    info_text = indexes.CharField(model_attr='info_text')
    description = indexes.CharField(model_attr='description')

    def get_model(self):
        return Staff

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
