from django.contrib import admin
from .models import Bookwishitem
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Bookwishitem)
class BookwishitemAdmin(SummernoteModelAdmin):

    list_display = ('listowner', 'booktitle', 'status', 'created_on', 'updated_on')
    search_fields = ['listowner', 'booktitle', 'status']
    list_filter = ('status', 'created_on')
    # prepopulated_fields = {'slug': ('booktitle',)}
    summernote_fields = ('personalnotes',)

# Register your models here.

