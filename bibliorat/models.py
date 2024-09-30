from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class BookProfile(models.Model):
    booktitle = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    profileauthor = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="book_profiles"
    )
    # bookwriter = models.ForeignKey(
    # BookAuthor, on_delete=models.CASCADE, related_name="book_authors"
    # )
    profilecontent = models.TextField()
    bookgenre = models.CharField(max_length=200, unique=True)
    publicationyear = models.CharField(max_length=200, unique=True)
    originallanguage = models.CharField(max_length=200, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    
