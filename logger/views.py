from django.shortcuts import (
    get_object_or_404,
    render,
)
from django.http import (
    HttpResponse,
    Http404,
    HttpResponseRedirect,
)
from django.urls import (
    reverse,
)
from django.views import (
    generic,
)

from .models import Read, Author, Book

class ListView(generic.ListView):
    def get_queryset(self):
        """Return the last five reads"""
        return Read.objects.order_by("-date")

def index(request):
    context = {
        'mediums': Read.MEDIUM_CHOICES,
    }
    return render(request, "logger/index.html", context)

class DetailView(generic.DetailView):
    model = Read
    template_name = "logger/detail.html"

def log(request):
    title = request.POST["title"]
    author = request.POST["author"]
    date = request.POST["date"]
    medium = request.POST["medium"]
    author = Author(name=author)
    author.save()
    book = Book(title=title, author=author)
    book.save()
    read = Read(book=book, date=date, medium=medium)
    read.save()
    return HttpResponseRedirect(reverse("logger:list"))
