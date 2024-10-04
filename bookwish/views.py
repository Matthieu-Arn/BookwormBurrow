from django.shortcuts import render, redirect, get_object_or_404
from .models import Bookwishitem
from bibliorat.models import Bookprofile

# Create your views here.
def mybookwishitems(request, slug):
    """
    Display an individual :model:`bookwish.Bookwishitem`.
    Renders the Bookwishitem page
    **Context**
    ``bookwishitem``
        An instance of :model:`bookwish.Bookwishitem`.
    **Template:**
    :template:`bookwish/bookwish.html`
    """
    if request.user.is_authenticated:
        bookprofile = get_object_or_404(Bookprofile, slug=slug)
        # Create a new wishlist item
        Bookwishitem.objects.get_or_create(listowner=request.user, booktitle=bookprofile)
    return redirect('bookprofile_detail', slug=slug)


def add_to_reading_list(request, slug):
    # Add item to wishlist
    if request.user.is_authenticated:
        bookprofile = get_object_or_404(Bookprofile, slug=slug)
        Bookwishitem.objects.get_or_create(listowner=request.user, booktitle=bookprofile)
    return redirect('bookprofile_detail', slug=slug)

def remove_from_reading_list(request, slug):
    # Remove item from wishlist
    if request.user.is_authenticated:
        bookprofile = get_object_or_404(Bookprofile, slug=slug)
        Bookwishitem.objects.filter(listowner=request.user, booktitle=bookprofile).delete()
    return redirect('bookprofile_detail', slug=slug)