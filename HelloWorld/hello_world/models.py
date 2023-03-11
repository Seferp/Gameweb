from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
# Create your models here.

# class User(models.Model):
#     id = models.IntegerField(primary_key=True, null=False, unique=True)
#     nickname = models.CharField(null=False, unique=True, MinLengthValidator=7, MaxLengthValidator=20)
#     password = models.CharField(null=False, MinLengthValidator=7, MaxLengthValidator=20)
#     email_address = models.EmailField()
#     country = models.CharField(max_length=50)
#     type_account = models.CharField(max_length=5)
#     counter_ratings = models.IntegerField()
class Category(models.Model):
    id = models.IntegerField(primary_key=True, null=False, unique=True)
    type = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.type
class Publisher(models.Model):
    id = models.IntegerField(primary_key=True, null=False, unique=True)
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Game(models.Model):
    id = models.IntegerField(primary_key=True, null=False, unique=True)
    title = models.CharField(max_length=100)
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True,)
    release_date = models.DateField()
    rating = models.FloatField()
    image = models.ImageField()

    def __str__(self):
        return self.title

class GameCategory(models.Model):
    id = models.IntegerField(primary_key=True, null=False, unique=True)
    id_game = models.ManyToManyField(Game)
    id_category = models.ManyToManyField(Category)
