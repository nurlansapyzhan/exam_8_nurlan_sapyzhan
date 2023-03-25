from django import forms

from reviewer.models import Product


class SearchForm(forms.Form):
    search = forms.CharField(max_length=30, required=False, label='Search')


class ProductForm(forms.ModelForm):
    CHOICES = (
        ('other', 'Other'),
        ('service', 'Service'),
        ('product', 'Product')
    )
    category = forms.ChoiceField(choices=CHOICES, initial='other', label='Category')

    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'category')
        labels = {
            'name': 'Product name',
            'description': 'Description',
            'image': 'Image URL',
            'category': 'Category'
        }
