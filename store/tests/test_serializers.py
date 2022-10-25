from django.test import TestCase

from store.models import Book
from store.serializers import BooksSerializer
from django.contrib.auth.models import User


class BookSerializerTestCase(TestCase):
    def test_ok(self):
        self.user = User.objects.create(username='test_username', )
        # print(User)
        book_1 = Book.objects.create(name='Test book 1', price=25,
                                     author_name='Author 1', owner=self.user.username)
        book_2 = Book.objects.create(name='Test book 2', price=55,
                                     author_name='Author 2', owner=self.user.username)
        data = BooksSerializer([book_1, book_2], many=True).data
        expected_data = [
            {
                'id': book_1.id,
                'name': 'Test book 1',
                'price': '25.00',
                'author_name': 'Author 1',
                'owner': self.user,
            },
            {
                'id': book_2.id,
                'name': 'Test book 2',
                'price': '55.00',
                'author_name': 'Author 2',
                'owner': self.user,
            },

        ]
        print(expected_data, data, sep='\n')

        self.assertEqual(expected_data, data)

