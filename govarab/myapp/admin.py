from django import forms
import myapp.translation
from modeltranslation.admin import TranslationAdmin
from django.contrib import admin
from .models import *


class ExampleAdmin(TranslationAdmin):
    pass


@admin.register(Product)
class ProductAdmin(ExampleAdmin, admin.ModelAdmin):
    formfield_overrides = {models.TextField: {'widget': forms.Textarea(attrs={'class': 'ckeditor'})}, }

    class Media:
        js = ('ckeditor/ckeditor.js',)


@admin.register(Gallery, ProductCategory, FAQ, Team, Slogan)
class ExampleAdmin(TranslationAdmin):
    pass

