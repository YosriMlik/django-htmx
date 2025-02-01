from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from .models import Book
from .forms import BookForm
from django.template.context_processors import csrf

def htmx_component(request, component, props=None):
    if props is None:
        props = {}

    # Add CSRF token to props if not already present
    props.update(csrf(request))

    if request.META.get('HTTP_HX_REQUEST'):
        print("============================== HTMX is available ==============================")
        return render(request, component, props)
    else:
        print("============================== HTMX is not available, rendering :", component+" ==============================")
        content = render_to_string(component, props)
        props['content'] = content
        return render(request, 'base.html', props)


# List all books
def book_list(request):
    books = Book.objects.all()
    form = BookForm()
    props = {'books': books, 'form': form, 'csrf_token': request.META.get('CSRF_COOKIE')}
    return htmx_component(request, 'books/book_list.html', props)


def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            return htmx_component(request, 'books/_book_item.html', {'book': book})
            #return redirect('book_list')
    else:
        return redirect('book_list')


# Update an existing book
def book_update(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return htmx_component(request, 'books/book_form.html', {'form': form})

# Delete a book
def book_delete(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return htmx_component(request, 'books/book_confirm_delete.html', {'book': book, 'csrf_token': request.META.get('CSRF_COOKIE')})
