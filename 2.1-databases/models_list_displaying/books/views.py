from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Book


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all().order_by('pub_date')
    context = {'books': books}
    return render(request, template, context)


def book_view(request, pub_date):
    """
    prev_page, next_page  - чтобы получить информацию о предыдущей, следующей страницах и достать pub_date
    для отображения ссылок в виде даты публикации.
    """
    template = 'books/books_list.html'
    books = Book.objects.all().order_by('pub_date')
    page_number = 0
    if not request.GET:
        for book in books:
            page_number += 1
            if str(book.pub_date) == pub_date:
                break
    else:
        page_number = int(request.GET.get('page', 0))

    paginator = Paginator(books, 1)
    page = paginator.get_page(page_number)
    prev_page = paginator.get_page(page_number - 1)
    next_page = paginator.get_page(page_number + 1)
    context = {'books': page,
               'prev_page': prev_page,
               'next_page': next_page
               }
    return render(request, template, context)