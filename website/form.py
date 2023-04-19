from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email please'}))
    first_Name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First name'}))
    last_Name = forms.CharField(label="",max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last name'}))


    class Meta:
        model = User
        fields = ('username', 'first_Name', 'last_Name', 'email', 'password1', 'password2')
        