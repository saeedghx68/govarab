from modeltranslation.translator import register, TranslationOptions
from myapp.models import *


@register(Gallery)
class GalleryTranslationOptions(TranslationOptions):
    fields = ('alt',)
    fallback_languages = {'default': ('fa',)}


@register(ProductCategory)
class ProductCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)
    fallback_languages = {'default': ('fa',)}


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name',)
    fallback_languages = {'default': ('fa',)}


@register(FAQ)
class FAQTranslationOptions(TranslationOptions):
    fields = ('question', 'answer',)
    fallback_languages = {'default': ('fa',)}


@register(Team)
class TeamTranslationOptions(TranslationOptions):
    fields = ('name', 'post',)
    fallback_languages = {'default': ('fa',)}
