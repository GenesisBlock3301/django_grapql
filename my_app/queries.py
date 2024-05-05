import graphene
from graphene_django import DjangoObjectType
from .models import Author, Book


class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        fields = ('id', 'name')


class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = ('id', 'name', 'authors')


class Query(graphene.ObjectType):
    """
    Query for restaurants model
    """
    authors = graphene.List(AuthorType)
    books = graphene.List(BookType)

    def resolve_authors(self, info, **kwargs):
        return Author.objects.all()

    def resolve_books(self, info, **kwargs):
        return Book.objects.all()