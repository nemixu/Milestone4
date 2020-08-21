from django import forms
from .models import UserProfile, Diary

class UserProfileForm(forms.ModelForm):
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
            

class DiaryEntry(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ('task_name','diary_text')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['task_name'].widget.attrs['autofocus'] = True
        self.fields['diary_text'].widget.attrs.update({'class': 'textarea', 'placeholder': 'What is your workout plans?'})
        
        
                    