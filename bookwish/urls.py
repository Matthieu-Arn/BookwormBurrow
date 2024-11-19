from . import views
from django.urls import path

urlpatterns = [
    path('', views.mybookwishitems, name='bookwish'),
    path('add/<slug:slug>/', views.add_to_reading_list, name='add_to_reading_list'),
    path('remove/<slug:slug>/', views.remove_from_reading_list, name='remove_from_reading_list'),
    path('my-list/', views.reading_list, name='reading_list'),
    path('remove-from-list/<int:item_id>/', views.remove_from_list, name='remove_from_list'),
    path('change-status/<int:item_id>/', views.change_status, name='change_status'),
    path('wishlist/<slug:slug>/', views.mybookwishitems, name='mybookwishitems'),
]