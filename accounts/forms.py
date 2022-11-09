from django import forms
from .models import User

class UserForm(forms.ModelForm):
     
    password = forms.CharField(widget=forms.TextInput(attrs={
        "type": "password",
        'placeholder': 'Password',
        'required': True
    }))
    confirm_password = forms.CharField(widget=forms.TextInput(attrs={
        "type": "password",
        'placeholder': 'Confirm password',
        'required': True
    }))
    first_name = forms.CharField(label="first_name", widget=forms.TextInput(attrs={
        'placeholder': 'First name',
        'required': True
    }))
    last_name = forms.CharField(label="last_name", widget=forms.TextInput(attrs={
        'placeholder': 'Last name',
        'required': True
    }))
    username = forms.CharField(label="username", widget=forms.TextInput(attrs={
        'placeholder': 'User name',
        'required': True
    }))
    email = forms.EmailField(label="email", widget=forms.TextInput(attrs={
        'placeholder': 'Email',
        'required': True
    }))
    confirm_accept = forms.BooleanField()
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'confirm_password', "confirm_accept"]

    def clean(self):
        clean_data = super(UserForm, self).clean()
        password = clean_data.get("password")
        confirm_password = clean_data.get("confirm_password")
        if len(password) < 8:
            raise forms.ValidationError(
                "password must at least 8 charactor"
            )
        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )