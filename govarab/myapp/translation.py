from modeltranslation.translator import register, TranslationOptions
from myapp.models import *


@register(Gallery)
class GalleryTranslationOptions(TranslationOptions):
    fields = ('alt',)


@register(ProductCategory)
class ProductCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)


@register(FAQ)
class FAQTranslationOptions(TranslationOptions):
    fields = ('question', 'answer',)


@register(Team)
class TeamTranslationOptions(TranslationOptions):
    fields = ('name', 'post',)
