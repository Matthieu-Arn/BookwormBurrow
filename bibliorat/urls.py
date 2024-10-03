from . import views
from django.urls import path
from .views import BookprofileList

urlpatterns = [
    path('', BookprofileList.as_view(), name='home'),
]