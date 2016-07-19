from django.contrib import admin
from pokemon.models import pokemon, user



class PokeAdmin(admin.ModelAdmin):
      list_display=['name', 'attack', 'defense', 'ptype', 'user']

class UserAdmin(admin.ModelAdmin):
      list_display=['name']


# Register your models here.
admin.site.register(pokemon, PokeAdmin)
admin.site.register(user, UserAdmin)