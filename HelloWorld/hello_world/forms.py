from django import forms

from .models import Category, Publisher

class PublisherForm(forms.ModelForm):
    class Meta:
        model: Publisher
        exclude = ['id']
        labels = {
            'name': 'Name',
            'country': 'Country'
        }

class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model: Category
        exclude = ['id']
        labels = {
            'type': 'Category type'
        }