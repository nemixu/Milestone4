from django import forms
from .models import Category, Product, Review


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'stripe-style-input rounded'
            

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review 
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea(
                attrs={
                    "rows": 5,
                    "class": 'form-control',
                    "placeholder": "Minimum 15 characters",
                }
            ),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comment'].label = "Leave a review"    
            