from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    """defines form to create users from font end"""
    first_name = forms.CharField
    last_name = forms.CharField
    email = forms.EmailField(required=True)
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')])
    account_type = forms.ChoiceField(choices=[('Service provider', 'Service provider'), ('Service seeker', 'Service seeker')])
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'gender', 'account_type', 'password1', 'password2']

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['profile_picture', 'about_me', 'profession', 'country', 'region', 'town', 'phone', 'available']
