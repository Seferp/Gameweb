from django.contrib import admin



from .models import Game, Category, Publisher,  GameCategory

# Register your models here.

class GamewebAdmin(admin.ModelAdmin):
    pass

admin.site.register(Game)
admin.site.register(Publisher)
admin.site.register(Category)
admin.site.register(GameCategory)

