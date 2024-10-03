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
    Bookauthor, on_delete=models.CASCADE, related_name="book_authors", default=True
    )
    bookhook = models.TextField(blank=True)
    profilecontent = models.TextField()
    bookgenre = models.CharField(max_length=30, unique=True)
    publicationyear = models.IntegerField()
    originallanguage = models.CharField(max_length=30, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    
class Bookauthor(models.Model):
    authorname = models.CharField(max_length=200, unique=True)
    authorbio = models.TextField(blank=True)
    # created_on = models.DateTimeField(auto_now_add=True)
    # status = models.IntegerField(choices=STATUS, default=0)

class Bookreview(models.Model):
    booktitle = models.ForeignKey(Bookprofile, on_delete=models.CASCADE)
    reviewauthor = models.ForeignKey(User, on_delete=models.CASCADE)
    reviewcontent = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

# class Readinglist(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     booktitle = models.ForeignKey(Bookprofile, on_delete=models.CASCADE)
#     created_on = models.DateTimeField(auto_now_add=True)
#     status = models.IntegerField(choices=STATUS, default=0)
