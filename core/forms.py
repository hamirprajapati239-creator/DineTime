from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserSignupForm(UserCreationForm):
    # Defining explicit fields to ensure we can control widgets easily
    firstname = forms.CharField(max_length=100)
    lastname = forms.CharField(max_length=100)
    age = forms.IntegerField()

    class Meta:
        model = User
        # 'password1' and 'password2' are handled by UserCreationForm automatically
        fields = ['email', 'role', 'firstname', 'lastname', 'age']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Professional UI Tweak: Add placeholders and classes dynamically
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'auth-input',
                'placeholder': ' '  # Required for the CSS :not(:placeholder-shown) logic
            })
            # Remove default Django help text for a cleaner look
            field.help_text = ''

class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'auth-input',
                'placeholder': ' '  # Required for the CSS animation
            })