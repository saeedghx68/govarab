from django import forms
import myapp.translation
from modeltranslation.admin import TranslationAdmin
from django.contrib import admin
from .models import *


class ExampleAdmin(TranslationAdmin):
    pass


admin.site.register(Gallery, ExampleAdmin)
admin.site.register(ProductCategory, ExampleAdmin)
admin.site.register(Product, ExampleAdmin)
admin.site.register(FAQ, ExampleAdmin)
admin.site.register(Team, ExampleAdmin)
