from django.contrib import admin
from pokemon.models import pokemon, user, capture



class PokeAdmin(admin.ModelAdmin):
      list_display=['name', 'attack', 'defense', 'ptype']

class UserAdmin(admin.ModelAdmin):
      list_display=['name']

class CapAdmin(admin.ModelAdmin):
      list_display=['user', 'pokemon', 'capture_location']


# Register your models here.
admin.site.register(pokemon, PokeAdmin)
admin.site.register(user, UserAdmin)
admin.site.register(capture, CapAdmin)