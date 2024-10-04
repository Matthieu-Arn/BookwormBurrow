from django.contrib import admin
from .models import Bookauthor, Bookprofile, Bookreview
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Bookprofile)
class BookprofileAdmin(SummernoteModelAdmin):

    list_display = ('booktitle', 'slug', 'authorname', 'status', 'profileauthor', 'publicationyear', 'originallanguage', 'bookgenre', 'created_on')
    search_fields = ['booktitle', 'profilesynopsis', 'profileanalysis']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('booktitle',)}
    summernote_fields = ('profilesynopsis', 'profileanalysis',)

@admin.register(Bookauthor)
class BookauthorAdmin(SummernoteModelAdmin):
    list_display = ('authorname', 'authorbio')
    search_fields = ['authorname', 'authorbio']
    summernote_fields = ('authorbio',)

# Register your models here.
# admin.site.register(Bookauthor)
admin.site.register(Bookreview)