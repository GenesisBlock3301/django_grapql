from .models import Author, Book
from django.test import TestCase, Client
import json


# UnitTest
class BookModelTest(TestCase):

    def setUp(self):
        self.author1 = Author.objects.create(name="Author1")
        self.author2 = Author.objects.create(name="Author2")

    def test_string_representation(self):
        book = Book(name="The Great Gatsby")
        self.assertEqual(str(book), book.name)

    def test_author_instance(self):
        self.assertEqual("Author1", self.author1.name)

    def test_book_creation(self):
        book = Book.objects.create(name="1984")
        book.authors.add(self.author1, self.author2)

        self.assertEqual(book.name, "1984")
        self.assertEqual(book.authors.count(), 2)
        self.assertIn(self.author1, book.authors.all())
        self.assertIn(self.author2, book.authors.all())


# Integration test
class GraphQLTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.author1 = Author.objects.create(name='Author One')
        self.author2 = Author.objects.create(name='Author Two')
        self.book1 = Book.objects.create(name='Book One')
        self.book1.authors.add(self.author1)
        self.book2 = Book.objects.create(name='Book Two')
        self.book2.authors.add(self.author2)

    def test_query_authors(self):
        response = self.client.post(
            '/graphql',
            json.dumps({
                'query': '''
                {
                    authors {
                        id
                        name
                    }
                }
                '''
            }),
            content_type='application/json'
        )
        content = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertIn('data', content)
        self.assertEqual(len(content['data']['authors']), 2)
        self.assertEqual(content['data']['authors'][0]['name'], 'Author One')

    def test_query_books(self):
        response = self.client.post(
            '/graphql',
            json.dumps({
                'query': '''
                {
                    books {
                        id
                        name
                        authors {
                            name
                        }
                    }
                }
                '''
            }),
            content_type='application/json'
        )
        content = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertIn('data', content)
        self.assertEqual(len(content['data']['books']), 2)
        self.assertEqual(content['data']['books'][0]['name'], 'Book One')
        self.assertEqual(content['data']['books'][0]['authors'][0]['name'], 'Author One')
