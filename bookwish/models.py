from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from bibliorat.models import Bookprofile

# User = get_user_model()

STATUS = ((0, "To read"), (1, "Read - Good"), (2, "Read - Not so good"))

# Create your models here.

class Bookwishitem(models.Model):
    listowner = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="wishlist"
    )
    booktitle = models.ForeignKey(
    Bookprofile, on_delete=models.CASCADE, related_name="wishlist"
    )
    profile_image = CloudinaryField('image', default='placeholder')
    personalnotes = models.TextField(default="Personal notes go here")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return f"{self.listowner.username}'s wishlist for {self.booktitle.booktitle}"
