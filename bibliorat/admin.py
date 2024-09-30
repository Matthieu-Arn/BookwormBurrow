from django.contrib import admin
from .models import Bookprofile
from .models import Bookauthor

# Register your models here.
admin.site.register(Bookprofile)
admin.site.register(Bookauthor)