from django.test import TestCase
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
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
        
    def test_password_whitespace_not_stripped(self):
        data = {
            'username': 'testuser',
            'password1': '   testpassword   ',
            'password2': '   testpassword   ',
        }
        form = UserCreationForm(data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['password1'], data['password1'])
        self.assertEqual(form.cleaned_data['password2'], data['password2'])
        
        