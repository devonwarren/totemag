from rest_framework import serializers
from articles.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    thumbnail_url = serializers.ReadOnlyField(source='image_thumbnail.url')
    url = serializers.ReadOnlyField(source='get_absolute_url')
    category = serializers.ReadOnlyField(source='category_name')

    class Meta:
        model = Article
        fields = ('id', 'title', 'url', 'thumbnail_url', 'category')
