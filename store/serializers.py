from rest_framework.serializers import ModelSerializer, SerializerMethodField

from store.models import Book, UserBookRelation


class BooksSerializer(ModelSerializer):
    likes_count = SerializerMethodField()
    class Meta:
        model = Book
        fields = ('id', 'name', 'price', 'author_name', 'likes_count')

    def get_likes_count(self, instance):
        return UserBookRelation.objects.filter(book=instance, like=True).count()


class UserBookRelationSerializer(ModelSerializer):
    class Meta:
        model = UserBookRelation
        fields = '__all__'
