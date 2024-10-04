from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import generic
from .models import Bookprofile

# Create your views here.

class BookprofileList(generic.ListView):
    queryset = Bookprofile.objects.filter(status=1).order_by('-created_on')
    template_name = 'bibliorat/index.html'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        # Calculate the second to last page
        paginator = context['paginator']
        if paginator.num_pages > 1:
            context['second_to_last_page'] = paginator.num_pages - 1
        else:
            context['second_to_last_page'] = None  

        return context

def bookprofile_detail(request, slug):
    """
    Display an individual :model:`bibliorat.Bookprofile`.

    **Context**

    ``bookprofile``
        An instance of :model:`bibliorat.Bookprofile`.

    **Template:**

    :template:`bibliorat/bookprofile_detail.html`
    """

    queryset = Bookprofile.objects.filter(status=1)
    bookprofile = get_object_or_404(queryset, slug=slug)
    bookreviews = bookprofile.bookreview_set.all().order_by("-created_on")
    bookreview_count = bookprofile.bookreview_set.filter(approved=True).count()
    
    return render(
        request,
        "bibliorat/bookprofile_detail.html",
        {"bookprofile": bookprofile,
        "bookreviews": bookreviews,
        "bookreview_count": bookreview_count,
        },
    )