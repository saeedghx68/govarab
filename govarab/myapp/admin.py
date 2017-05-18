from django.contrib import admin
from .models import *
from django import forms


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


# #************* Product Admin *****************
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline, ]
    formfield_overrides = {models.TextField: {'widget': forms.Textarea(attrs={'class': 'ckeditor'})}, }

    class Media:
        js = ('ckeditor/ckeditor.js',)


# #************* ProductCategory Admin *****************
class ProductCategorytAdmin(admin.ModelAdmin):
    formfield_overrides = {models.TextField: {'widget': forms.Textarea(attrs={'class': 'ckeditor'})}, }

    class Media:
        js = ('ckeditor/ckeditor.js',)


# #************* ProductCategory Admin *****************
class ProductUsertAdmin(admin.ModelAdmin):
    formfield_overrides = {models.TextField: {'widget': forms.Textarea(attrs={'class': 'ckeditor'})}, }

    class Media:
        js = ('ckeditor/ckeditor.js',)


# #************* About Admin *****************
class AboutAdmin(admin.ModelAdmin):
    formfield_overrides = {models.TextField: {'widget': forms.Textarea(attrs={'class': 'ckeditor'})}, }

    class Media:
        js = ('ckeditor/ckeditor.js',)


admin.site.register(About, AboutAdmin)
admin.site.register(Gallery)
admin.site.register(ProductCategory, ProductCategorytAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Team)
