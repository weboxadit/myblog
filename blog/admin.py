from django.contrib import admin

from .models import Blog, Category

# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    exclude = ['posted']
    populated_fields = {'slug': 'title,'}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': 'title,'}



admin.site.register(Blog)
admin.site.register(Category)



