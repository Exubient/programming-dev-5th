from django.contrib import admin
from pokemon.models import pokemon, user, capture, location



class PokeAdmin(admin.ModelAdmin):
      list_display=['name', 'attack', 'defense', 'ptype']

class UserAdmin(admin.ModelAdmin):
      list_display=['name']

class CapAdmin(admin.ModelAdmin):
      list_display=['user', 'pokemon', 'location']

class LocAdmin(admin.ModelAdmin):
      list_display=['name', 'lnglat', 'created_at']



# Register your models here.
admin.site.register(pokemon, PokeAdmin)
admin.site.register(user, UserAdmin)
admin.site.register(capture)
admin.site.register(location, LocAdmin)