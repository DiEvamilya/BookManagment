"""
URL configuration for BookManagment project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from BookManagmentapp.views import StartPageView, BookListView, AuthorListView, BookCreateView, AuthorCreateView, \
    BookDetailView, BookUpdateView, BookDeleteView, AuthorUpdateView, AuthorDetailView, AuthorDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', StartPageView.as_view(), name='start'),
    path('book-list/', BookListView.as_view(), name='book_list'),
    path('author-list/', AuthorListView.as_view(), name='author_list'),
    path('add-book/', BookCreateView.as_view(), name='add_book'),
    path('add-author/', AuthorCreateView.as_view(), name='add_author'),
    path('update-book/<slug:slug>', BookUpdateView.as_view(), name='update_book'),
    path('book-detail/<slug:slug>/', BookDetailView.as_view(), name='book_detail'),
    path('book-delete/<slug:slug>', BookDeleteView.as_view(), name='book_delete'),
    path('update-author/<str:pk>', AuthorUpdateView.as_view(), name='update_author'),
    path('author-delete/<str:pk>', AuthorDeleteView.as_view(), name='author_delete'),
    path('author-detail/<str:pk>', AuthorDetailView.as_view(), name='author_detail'),
 ]
