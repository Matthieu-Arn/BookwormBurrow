from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Bookprofile(models.Model):
    booktitle = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    profileauthor = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="book_profiles"
    )
    authorname = models.ForeignKey(
    "BookAuthor", on_delete=models.CASCADE, related_name="book_authors", default=True
    )
    bookhook = models.TextField(blank=True)
    profilecontent = models.TextField()
    bookgenre = models.CharField(max_length=30, unique=True)
    publicationyear = models.IntegerField()
    originallanguage = models.CharField(max_length=30, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    
class Bookauthor(models.Model):
    authorname = models.CharField(max_length=200, unique=True)
    authorbio = models.TextField(blank=True)
    # created_on = models.DateTimeField(auto_now_add=True)
    # status = models.IntegerField(choices=STATUS, default=0)
