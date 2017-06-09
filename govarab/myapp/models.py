# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


# from easymode.i18n.decorators import I18n


class Gallery(models.Model):
    small_img = models.ImageField(default='images/gallery/defaults.jpg', upload_to='images/gallery/',
                                  verbose_name=_('small image'))
    large_img = models.ImageField(default='images/gallery/defaults.jpg', upload_to='images/gallery/',
                                  verbose_name=_('large image'))
    alt = models.CharField(default='', max_length=100, verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True)

    def as_json(self):
        return {
            'id': self.id - 1,
            'imgs': str(self.small_img),
            'imgl': str(self.large_img),
            'alt': self.alt,
        }

    def __unicode__(self):
        return self.alt

    class Meta:
        ordering = ['created_at']
        verbose_name = _('Gallery')
        verbose_name_plural = _('Gallery')


# #*****************End of gallery model********************

class SlidesImages(models.Model):
    img = models.ImageField(default='images/slides/defaults.jpg', upload_to='images/slides/',
                                  verbose_name=_('image'))

    def __unicode__(self):
        return str(self.img)

    class Meta:
        verbose_name = _('Slides image')
        verbose_name_plural = _('Slides Images')


# #*****************End of gallery model********************


class ProductCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('category name'))

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('Product Category')
        verbose_name_plural = _('Product Category')


# #******************End of Product Category ********************

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('product name'))
    category = models.ForeignKey(ProductCategory, verbose_name=_('product category'), related_name='productCat')
    description = models.TextField(verbose_name=_('description'), default="")
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')


# #******************End of Product ********************

class ProductImage(models.Model):
    product = models.ForeignKey(Product, verbose_name=_('product'), related_name='images')
    small_img = models.ImageField(upload_to='images/products/', verbose_name=_('small image'),
                                  help_text='size(500px * 334px)', default='images/products/defaults.jpg')
    big_img = models.ImageField(upload_to='images/products/', verbose_name=_('large image'),
                                default='images/products/defaults.jpg')
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.product.name

    class Meta:
        ordering = ['created_at']
        verbose_name = _('Product Image')
        verbose_name_plural = _('Products Images')
# #******************End of Product ********************


class FAQ(models.Model):
    question = models.TextField(verbose_name=_('question'))
    answer = models.TextField(verbose_name=_('answer'))
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.question

    class Meta:
        ordering = ['updated_at']
        verbose_name = _('FAQ')
        verbose_name_plural = _('FAQs')


# #******************End of Product Category ********************

# @I18n('post')
class Team(models.Model):
    name = models.CharField(max_length=500, verbose_name=_('name'))
    post = models.CharField(max_length=500, verbose_name=_('post'), default="")
    file = models.FileField(upload_to='resume/', max_length=100, verbose_name=_('CV'))
    email = models.EmailField(verbose_name=_('email'))
    image = models.ImageField(blank=True, null=True, upload_to='images/team/', verbose_name=_('image'),
                              help_text='size(260*311)')
    priority = models.IntegerField(default=1, verbose_name=_('priority'))

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('Team')
        verbose_name_plural = _('Team')


# #******************End of Product Category ********************
class Slogan(models.Model):
    text = models.CharField(max_length=1200, verbose_name=_('text'))
    priority = models.IntegerField(verbose_name=_('priority'))

    def __unicode__(self):
        return self.text

    class Meta:
        verbose_name = _('Slogan')
        verbose_name_plural = _('Slogan')


# ******************End of Product Category ********************


class Catalog(models.Model):
    title = models.CharField(default='', max_length=100, verbose_name=_('title'))
    file = models.FileField(upload_to='catalog/', max_length=100, verbose_name=_('file'))

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _('catalog')
        verbose_name_plural = _('catalog')
# ******************End of catalog ********************


class Article(models.Model):
    title = models.CharField(default='', max_length=100, verbose_name=_('title'))
    text = models.TextField(verbose_name=_('text'))
    image = models.ImageField(blank=True, null=True, upload_to='images/articles/', verbose_name=_('image'))
    link = models.URLField(verbose_name=_('source link'))
    created_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['created_at']
        verbose_name = _('article')
        verbose_name_plural = _('articles')
# ******************End of articles ********************
