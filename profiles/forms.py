from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    """
    Form to generate the user profile form
    """
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field"""
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_full_name': 'Full Name',
            'default_email': 'Email',
            'default_phone_number': 'Phone Number',
        }

        self.fields['default_full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'rounded stripe-style-input form-styling'
            self.fields[field].label = False
            