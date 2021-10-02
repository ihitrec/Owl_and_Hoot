from django import forms
from .models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            "img": "Image URL",
        }
        exclude = ['num_of_ratings', 'total_rating']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['rating'].widget.attrs.update({
            'min': '0',
            'max': '5',
        })
