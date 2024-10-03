from django.shortcuts import render
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
            context['second_to_last_page'] = None  # No second to last page available

        return context