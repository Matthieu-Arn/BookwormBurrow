from django.shortcuts import render
from .models import Bookwishitem


# Create your views here.
def mybookwishitems(request):
    """
    Display an individual :model:`bookwish.Bookwishitem`.
    Renders the Bookwishitem page

    **Context**

    ``bookwishitem``
        An instance of :model:`bookwish.Bookwishitem`.

    **Template:**

    :template:`bookwish/bookwish.html`
    """
    
    bookwish = Bookwishitem.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "bookwish/bookwish.html",
        {"bookwish": bookwish},
    )

