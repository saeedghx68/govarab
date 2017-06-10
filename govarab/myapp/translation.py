from modeltranslation.translator import register, TranslationOptions
from myapp.models import *


@register(Gallery)
class GalleryTranslationOptions(TranslationOptions):
    fields = ('alt',)

@register(SlidesImages)
class TeamTranslationOptions(TranslationOptions):
    fields = ()

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

@register(Slogan)
class TeamTranslationOptions(TranslationOptions):
    fields = ('text',)

@register(Catalog)
class TeamTranslationOptions(TranslationOptions):
    fields = ()

@register(Article)
class TeamTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)

@register(Dealership)
class TeamTranslationOptions(TranslationOptions):
    fields = ('name', 'address', 'description',)
