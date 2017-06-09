from django import forms
import myapp.translation
from modeltranslation.admin import TranslationAdmin
from django.contrib import admin
from .models import *


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class ExampleAdmin(TranslationAdmin):
    pass


@admin.register(Product)
class ProductAdmin(ExampleAdmin, admin.ModelAdmin):
    inlines = [ProductImageInline, ]
    formfield_overrides = {models.TextField: {'widget': forms.Textarea(attrs={'class': 'ckeditor'})}, }

    class Media:
        js = ('ckeditor/ckeditor.js',)


@admin.register(Article)
class ArticleAdmin(ExampleAdmin, admin.ModelAdmin):
    formfield_overrides = {models.TextField: {'widget': forms.Textarea(attrs={'class': 'ckeditor'})}, }

    class Media:
        js = ('ckeditor/ckeditor.js',)


@admin.register(Gallery, ProductCategory, FAQ, Team, Slogan, Catalog, SlidesImages)
class ExampleAdmin(TranslationAdmin):
    pass
