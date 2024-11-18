from django.test import TestCase
from bibliorat.forms import BookreviewForm


# Form Tests for bibliorat
class TestBookreviewForm(TestCase):

    def test_form_is_valid(self):
        bookreview_form = BookreviewForm({'reviewcontent': 'This is a great book'})
        self.assertTrue(bookreview_form.is_valid())