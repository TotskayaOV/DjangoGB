from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'count', 'image']
        labels = {'name': 'Наименование',
                  'description': 'Описание',
                  'price': 'Цена',
                  'count': 'Количество на складе',
                  'image': 'Фото товара'}
