from uuid import uuid4

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models, IntegrityError
from django.utils.text import slugify


class Author(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255, primary_key=True)

    def __str__(self):
        return f'{self.name} - {self.surname}'


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255, primary_key=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    year_of_publication = models.DateField()
    genres = models.ManyToManyField(Genre, related_name='books')
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])

    def __str__(self):
        return f"{self.title} "

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f' {self.title}')

        while True:
            try:
                super().save(*args, **kwargs)
                break
            except IntegrityError:
                self.slug = f'{self.slug}-{str(uuid4())[:8]}'
        return super().save()