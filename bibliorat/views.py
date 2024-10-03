from django.shortcuts import render
# from django.http import HttpResponse
from django.views import generic
from .models import Bookprofile

# Create your views here.
# def my_blog(request):
    # return HttpResponse("Hello, Bibliorat!")
class BookprofileList(generic.ListView):
    # model = Bookprofile
    queryset = Bookprofile.objects.filter(status=1).order_by('?')
    # template_name = 'bibliorat/home.html'
    context_object_name = 'bookprofiles'