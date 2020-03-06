from django.test import TestCase
from .models import Page
# Create your tests here.

class PageTestCase(TestCase):
    def test_true_is_true(self):
        """ Tests if True is equal to True. Should always pass. """
        self.assertEqual(True, True)
        
    # def test_string_representation(self):
    #     entry = Page(recipe_title="My entry title")
    #     self.assertEqual(str(entry), Page.recipe_title)
        
    def test_verbose_name_plural(self):
        self.assertEqual(str(Page._meta.verbose_name_plural), "pages")