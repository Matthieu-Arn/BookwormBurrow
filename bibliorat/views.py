from django.shortcuts import render
# from django.http import HttpResponse
from django.views import generic
from .models import Bookprofile

# Create your views here.

class BookprofileList(generic.ListView):
    queryset = Bookprofile.objects.filter(status=1).order_by('?')
    template_name = 'bibliorat/index.html'
    # context_object_name = 'bookprofiles'
    paginate_by = 6