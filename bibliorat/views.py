from django.shortcuts import render, get_object_or_404, reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Bookprofile, Bookreview, Bookauthor
from .forms import BookreviewForm

# Create your views here.

class BookprofileList(generic.ListView):
    queryset = Bookprofile.objects.filter(status=1).order_by('-authorname')
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

    bookauthor = bookprofile.authorname

    if request.method == "POST":
        bookreview_form = BookreviewForm(data=request.POST)
        if bookreview_form.is_valid():
            bookreview = bookreview_form.save(commit=False)
            bookreview.reviewauthor = request.user
            bookreview.booktitle = bookprofile
            bookreview.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Review submitted and awaiting approval'
            )

    bookreview_form = BookreviewForm()
    
    return render(
        request,
        "bibliorat/bookprofile_detail.html",
        {"bookprofile": bookprofile,
        "bookreviews": bookreviews,
        "bookreview_count": bookreview_count,
        "bookreview_form": bookreview_form,
        "bookauthor": bookauthor,
        },
    )

def bookreview_edit(request, slug, bookreview_id):
    """
    view to edit a bookreview
    """
    if request.method == "POST":

        queryset = Bookprofile.objects.filter(status=1)
        bookprofile = get_object_or_404(queryset, slug=slug)
        bookreview = get_object_or_404(Bookreview, pk=bookreview_id)
        bookreview_form = BookreviewForm(data=request.POST, instance=bookreview)

        if bookreview_form.is_valid() and bookreview.reviewauthor == request.user:
            bookreview = bookreview_form.save(commit=False)
            bookreview.bookprofile = bookprofile
            bookreview.approved = False
            bookreview.save()
            messages.add_message(request, messages.SUCCESS, 'Your review has been updated!')
        else:
            messages.add_message(request, messages.ERROR, 'An error occurred while updating review!')

    return HttpResponseRedirect(reverse('bookprofile_detail', args=[slug]))

def bookreview_delete(request, slug, bookreview_id):
    """
    view to delete a bookreview
    """
    queryset = Bookprofile.objects.filter(status=1)
    bookprofile = get_object_or_404(queryset, slug=slug)
    bookreview = get_object_or_404(Bookreview, pk=bookreview_id)

    if bookreview.reviewauthor == request.user:
        bookreview.delete()
        messages.add_message(request, messages.SUCCESS, 'Your review has been deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own reviews!')

    return HttpResponseRedirect(reverse('bookprofile_detail', args=[slug]))

