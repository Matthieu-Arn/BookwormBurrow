from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Bookauthor(models.Model):
    authorname = models.CharField(max_length=200, unique=True)
    authorbio = models.TextField(blank=True)
    # created_on = models.DateTimeField(auto_now_add=True)
    # status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["authorname"]

    def __str__(self):
        return f"{self.authorname}"


class Bookprofile(models.Model):
    booktitle = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    profileauthor = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="book_profiles"
    )
    authorname = models.ForeignKey(
    Bookauthor, on_delete=models.CASCADE, related_name="book_authors"
    )
    bookhook = models.TextField(blank=True)
    profilesynopsis = models.TextField(default="Synopsis goes here")
    profileanalysis = models.TextField(default="Analysis goes here")
    bookgenre = models.CharField(max_length=30, unique=True)
    publicationyear = models.IntegerField()
    originallanguage = models.CharField(max_length=30, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_on"]
    
    def __str__(self):
        return f"{self.booktitle} by {self.authorname}, profiled by {self.profileauthor}"


class Bookreview(models.Model):
    booktitle = models.ForeignKey(Bookprofile, on_delete=models.CASCADE)
    reviewauthor = models.ForeignKey(User, on_delete=models.CASCADE)
    reviewcontent = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"A review by {self.reviewauthor} of {self.booktitle}"


# class Readinglist(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     booktitle = models.ForeignKey(Bookprofile, on_delete=models.CASCADE)
#     created_on = models.DateTimeField(auto_now_add=True)
#     status = models.IntegerField(choices=STATUS, default=0)
