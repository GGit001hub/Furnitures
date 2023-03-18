from django.contrib import admin
from .models import Mebel,Savat,Photo
# Register your models here.


class PhotoAdmin(admin.StackedInline):
    model = Photo



@admin.register(Mebel)
class MebelAdmin(admin.ModelAdmin):
    list_display = ['name','turi','addres','narx','id']
    list_filter = ['turi','addres']
    inlines = [PhotoAdmin]

    class Meta:
        model = Mebel



@admin.register(Savat)
class SavatAdmin(admin.ModelAdmin):
    list_display = ['product','miqdori','summa']

