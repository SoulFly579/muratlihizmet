from django.contrib import admin
from home.models import Category, Haberler , Setting , Image

# Register your models here.
class HaberAdmin(admin.ModelAdmin):
    list_display = ['title','author']

class ImageAdmin(admin.ModelAdmin):
    list_display = ['author']



admin.site.register(Category)
admin.site.register(Haberler, HaberAdmin)
admin.site.register(Setting)
admin.site.register(Image,ImageAdmin)