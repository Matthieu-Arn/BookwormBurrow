from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from bibliorat.models import Bookauthor, Bookprofile
from bibliorat.forms import BookreviewForm


# Create your tests here.

class TestBookprofileViews(TestCase):

    def setUp(self):
        # Create a superuser for authentication
        self.user = User.objects.create_superuser(
            username="myUsername11",
            password="myPassword",
            email="test@test.com"
        )

        # Create a Bookauthor instance
        self.book_author = Bookauthor.objects.create(
            authorname="U.N. Owen",
        )

        # Create a Bookprofile instance
        self.bookprofile = Bookprofile.objects.create(
            booktitle="Book title", 
            slug="book-title", 
            profileauthor=self.user,
            authorname=self.book_author,
            bookhook="A gripping story!",
            profilesynopsis="Gripping synopsis goes here",
            profileanalysis="Profound analysis goes here",
            bookgenre="Testing",
            publicationyear=2025,
            originallanguage="English",
            status=1,
        )

    def test_render_bookprofile_detail_page_with_review_form(self):
        url = reverse('bookprofile_detail', args=['book-title'])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        
        # Check that the book title, synopsis and analysis are present
        self.assertContains(response, "Book title")
        self.assertContains(response, "Gripping synopsis goes here")
        self.assertContains(response, "Profound analysis goes here")

        # Ensure the book review form is in the context
        self.assertIsInstance(response.context['bookreview_form'], BookreviewForm)

        # Check that the reviews and review count are passed correctly
        self.assertEqual(response.context['bookreviews'].count(), 0)  # No reviews yet
        self.assertEqual(response.context['bookreview_count'], 0)  # No approved reviews

