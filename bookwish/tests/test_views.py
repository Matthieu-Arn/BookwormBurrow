from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from bibliorat.models import Bookauthor, Bookprofile
from bibliorat.forms import BookreviewForm
from bookwish.views import mybookwishitems
from bookwish.models import Bookwishitem


class TestBookwishitemViews(TestCase):

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
            booktitle='Test Book',
            slug='test-book',
            profileauthor=self.user, 
            authorname=self.book_author,
            bookgenre='Fiction',
            publicationyear=2025,
            originallanguage='English'
        )
    
    def test_add_book_to_wishlist(self):
        # Login as the test user
        self.client.login(username='myUsername11', password='myPassword')
        
        # Construct the URL for the mybookwishitems view
        url = reverse('mybookwishitems', args=[self.bookprofile.slug])

        # Send a GET request to the view to add the book to the wishlist
        response = self.client.get(url)

        # Check that a Bookwishitem was created for the user and the bookprofile
        self.assertEqual(Bookwishitem.objects.count(), 1)
        bookwishitem = Bookwishitem.objects.first()
        self.assertEqual(bookwishitem.listowner, self.user)
        self.assertEqual(bookwishitem.booktitle, self.bookprofile)
        
    def test_add_book_to_wishlist_unauthenticated_user(self):
        # Send a GET request without being logged in
        url = reverse('mybookwishitems', args=[self.bookprofile.slug])
        response = self.client.get(url)
      
        # Ensure no Bookwishitem was created
        self.assertEqual(Bookwishitem.objects.count(), 0)