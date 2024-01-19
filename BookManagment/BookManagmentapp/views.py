
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DetailView, DeleteView, UpdateView

from BookManagmentapp.forms import BookForm, AuthorForm
from BookManagmentapp.models import Book, Author, Genre


class StartPageView(TemplateView):
    template_name = 'BookManagmentapp/start.html'


class BookListView(ListView):
    model = Book
    template_name = 'BookManagmentapp/book_list.html'
    context_object_name = 'book_list'

    def get_queryset(self):
        return Book.objects.all().order_by('title')


class AuthorListView(ListView):
    model = Author
    template_name = 'BookManagmentapp/author_list.html'
    context_object_name = 'author_list'

    def get_queryset(self):
        return Author.objects.all().order_by('surname')

class BookCreateView(CreateView):
    form_class = BookForm
    template_name = 'BookManagmentapp/add_book.html'
    success_url = reverse_lazy('book_list')

    def form_valid(self, form):
        return super().form_valid(form)

class AuthorCreateView(CreateView):
    form_class = AuthorForm
    template_name = 'BookManagmentapp/add_author.html'
    success_url = reverse_lazy('author_list')

    def form_valid(self, form):
        return super().form_valid(form)

class BookDetailView(DetailView):
    model = Book
    template_name = 'BookManagmentapp/book_detail.html'
    include = ['slug']
    slug_url_kwarg = 'slug'

class AuthorUpdateView(UpdateView):
    model = Author
    fields = '__all__'
    template_name = 'BookManagmentapp/update_author.html'
    success_url = reverse_lazy('author_list')
    context_object_name = "author"

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'BookManagmentapp/author_detail.html'
    success_url = reverse_lazy('author_list')

class BookDeleteView(DeleteView):
    template_name = 'BookManagmentapp/delete_book.html'
    model = Book
    success_url = reverse_lazy('book_list')
    context_object_name = "book"

class AuthorDeleteView(DeleteView):
    template_name = 'BookManagmentapp/delete_author.html'
    model = Author
    success_url = reverse_lazy('author_list')
    context_object_name = "author"

class BookUpdateView(UpdateView):
    model = Book
    template_name = 'BookManagmentapp/update_book.html'
    fields = '__all__'
    include = ['slug']
    success_url = reverse_lazy('book_list')
    context_object_name = "book"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genres'] = Genre.objects.all()
        context['current_page'] = self.request.GET.get('page')
        return context

    def form_valid(self, form):
        return super().form_valid(form)



