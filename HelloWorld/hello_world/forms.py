from django import forms

from .models import Category, Publisher, Game

class CreatePublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        exclude = ['id']
        labels = {
            "name": 'Name',
            "country": 'Country'
        }
    def clean_name(self):
        return self.cleaned_data['name'].capitalize()

class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = ['id']
        labels = {
            'type': 'Category type'
        }

class CreateGameForm(forms.ModelForm):
    class Meta:
        model = Game
        exclude = ['id']
        labels = {
            "title": "Game Title",
            "publisher": "Publisher name",
            "release_date": "Release Date",
            "rating": "Rating"
        }
    def clean_title(self):
        return self.cleaned_data['title'].capitalize()
