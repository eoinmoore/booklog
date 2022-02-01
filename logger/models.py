from django.db.models import (
    Model,
    CharField,
    DateTimeField,
    ForeignKey,
    CASCADE,
    PROTECT
)

class Author(Model):
    name = CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(Model):
    title = CharField(max_length=200)
    author = ForeignKey(Author, CASCADE)

    def __str__(self):
        return "'%s', %s" % (self.title, self.author)

class Read(Model):
    book = ForeignKey(Book, PROTECT)
    date = DateTimeField()
    PRINT_BOOK = "BK"
    EBOOK = "EB"
    AUDIOBOOK = "AB"
    GRAPHIC_NOVEL = "GN"
    MEDIUM_CHOICES = [
        (PRINT_BOOK, "Print Book"),
        (EBOOK, "E-book"),
        (AUDIOBOOK, "Audiobook"),
        (GRAPHIC_NOVEL, "Graphic Novel"),
    ]
    medium = CharField(
        max_length=2,
        choices=MEDIUM_CHOICES,
        default=PRINT_BOOK,
    )

    def description(self):
        return "Read '%s' by %s (%s) on %s" % (
                self.book.title, self.book.author,
                self.get_medium_display(), self.date.strftime("%Y/%m/%d"))

    def __str__(self):
        return "%s, %s, %s" % (self.book, self.date.strftime("%Y/%m/%d"), self.medium)
