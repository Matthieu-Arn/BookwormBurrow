from . import views
from django.urls import path

urlpatterns = [
    path('', views.mybookwishitems, name='bookwish'),
    path('add/<slug:slug>/', views.add_to_reading_list, name='add_to_reading_list'),
    path('remove/<slug:slug>/', views.remove_from_reading_list, name='remove_from_reading_list'),
]