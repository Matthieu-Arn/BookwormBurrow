from django.contrib import admin
from .models import Bookauthor, Bookprofile, Bookreview

# Register your models here.
admin.site.register(Bookauthor)
admin.site.register(Bookprofile)
admin.site.register(Bookreview)