from rest_framework import serializers
from book_api.models import Book

class BookSerializer(serializers.Serializer):
    """Serializer for the Book model.

    This serializer handles the conversion of Book instances to and from 
    JSON format. It includes fields for id, title, number of pages, 
    publish date, quantity, and author.

    Attributes:
        id (IntegerField): The unique identifier for the book.
        title (CharField): The title of the book.
        number_of_pages (IntegerField): The number of pages in the book.
        publish_date (DateField): The date the book was published.
        quantity (IntegerField): The quantity of the book available.
        author (CharField): The author of the book.
    """
    id=serializers.IntegerField(read_only=True)
    title=serializers.CharField()
    number_of_pages=serializers.IntegerField()
    publish_date=serializers.DateField()
    quantity=serializers.IntegerField()
    author=serializers.CharField()

    def create(self,data):
        return Book.objects.create(**data)

    def update(self,instance,data):
        instance.title=data.get('title',instance.title)
        instance.number_of_pages=data.get('number_of_pages',instance.number_of_pages)
        instance.publish_date=data.get('publish_date',instance.publish_date)
        instance.quantity=data.get('quantity',instance.quantity)
        instance.author=data.get('author',instance.author)

        instance.save()
        return instance