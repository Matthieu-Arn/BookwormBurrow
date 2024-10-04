from . import views
from django.urls import path
from .views import BookprofileList

urlpatterns = [
    path('', BookprofileList.as_view(), name='home'),
    path('<slug:slug>/', views.bookprofile_detail, name='bookprofile_detail'),
    path('<slug:slug>/edit_bookreview/<int:bookreview_id>',
         views.bookreview_edit, name='bookreview_edit'),
]