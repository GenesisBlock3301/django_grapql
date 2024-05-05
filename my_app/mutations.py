import graphene
from .models import Author, Book
from .queries import AuthorType, BookType


class CreateAuthor(graphene.Mutation):
    class Arguments:
        name = graphene.String()

    ok = graphene.Boolean()
    author = graphene.Field(AuthorType)

    def mutate(self, info, name):
        author = Author.objects.create(name=name)
        return CreateAuthor(ok=True, author=author)


class CreateBook(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        author_ids = graphene.List(graphene.ID, required=True)

    book = graphene.Field(BookType)

    def mutate(self, info, name, author_ids):
        authors = Author.objects.filter(id__in=author_ids)
        book = Book(name=name)
        book.save()
        book.authors.set(authors)
        return CreateBook(book=book)


class Mutation(graphene.ObjectType):
    create_author = CreateAuthor.Field()
    create_book = CreateBook.Field()