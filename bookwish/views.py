from django.shortcuts import render, redirect, get_object_or_404
from .models import Bookwishitem
from bibliorat.models import Bookprofile

# Create your views here.
def mybookwishitems(request, slug):
    if request.user.is_authenticated:
        bookprofile = get_object_or_404(Bookprofile, slug=slug)
        # Create a new wishlist item
        Bookwishitem.objects.get_or_create(listowner=request.user, booktitle=bookprofile)
    return redirect('bookprofile_detail', slug=slug)


def reading_list(request): 
    """
    Display an individual :model:`bookwish.Bookwishitem`.
    Renders the Readinglist page
    **Context**
    ``reading_list_item``
        An instance of :model:`bookwish.Bookwishitem`.
    **Template:**
    :template:`bookwish/reading_list.html`
    """
    if request.user.is_authenticated:
        reading_list_items = Bookwishitem.objects.filter(listowner=request.user).select_related('booktitle')
        return render(request, 'bookwish/reading_list.html', {'reading_list_items': reading_list_items})
    return redirect('login')  # Redirect to login if not authenticated


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


def remove_from_list(request, item_id):
    if request.method == "POST":
        item = get_object_or_404(Bookwishitem, id=item_id)
        item.delete()
    return redirect('reading_list')

def change_status(request, item_id):
    if request.method == "POST":
        item = get_object_or_404(Bookwishitem, id=item_id)
        new_status = request.POST.get('status')
        if new_status in ['0', '1', '2']:
            item.status = int(new_status)
            item.save()
    return redirect('reading_list')