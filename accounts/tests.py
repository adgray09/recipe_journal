from django.test import TestCase
from django.contrib.auth.forms import UserCreationForm
# Create your tests here.

class UserCreationFormTest(TestCase):
    # tests if form authenciation is working
    
    def test_form(self):
        data = {
            'username': 'testuser',
            'password1': 'Test991231',
            'password2': 'Test991231',
        }

        form = UserCreationForm(data)
        
        self.assertTrue(form.is_valid())
        
        