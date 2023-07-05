

from django.contrib import admin
from .models import Category,Product
# Register your models here.



class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ist_display = ['name', 'price','available','stock','updated','created']
    list_editable = ['price','stock','available']
    prepopulated_fields = {'slug':('name',)}
    List_per_page =20
admin.site.register(Product,ProductAdmin)
