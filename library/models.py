from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator



# Create your models here.
class Author (models.Model):
    name = models.CharField(max_length=200)
    birth_day = models.DateField()
    biography = models.TextField(max_length = 2000)

    def __str__(self):
        return self.name
    
class Book (models.Model):
    title = models.CharField(max_length = 300)
    publication_date = models.DateTimeField(default=timezone.now)
    price = models.FloatField()

    author = models.ForeignKey(Author, related_name = 'book_author', on_delete = models.CASCADE)    
    
    def __str__(self):
        return self.title


class Review (models.Model) :
    reviewer_name = models.CharField(max_length = 300)
    content = models.TextField(max_length = 2000)
    rating = models.IntegerField(default=1,validators=[MaxValueValidator(5), MinValueValidator(1)])

    book = models.ForeignKey(Book, related_name= 'review_book', on_delete = models.CASCADE)

    def __str__(self):
        return str(self.book)
    