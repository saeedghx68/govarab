# -*- coding: utf-8 -*-
from django.db import models


class About(models.Model):
    description = models.TextField(verbose_name=u'متن درباره ما')
    tel = models.CharField(max_length=65, verbose_name=u'تلفن')
    mobile = models.CharField(max_length=50, verbose_name=u'موبایل')
    address = models.CharField(max_length=250, verbose_name=u'آدرس')

    class Meta:
        verbose_name = u'درباره ما'
        verbose_name_plural = u'درباره ما'
# *****************End of about us model********************


class Gallery(models.Model):
    small_img = models.ImageField(default='images/gallery/defaults.jpg', upload_to='images/gallery/',
                                  verbose_name=u'تصویر کوچک')
    large_img = models.ImageField(default='images/gallery/defaults.jpg', upload_to='images/gallery/',
                                  verbose_name=u'تصویر بزرگ')
    alt = models.CharField(default='', max_length=100, verbose_name=u'عنوان')
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
        verbose_name = u'گالری تصاویر'
        verbose_name_plural = u'گالری تصاویر'
# #*****************End of gallery model********************


class ProductCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'دسته اصلی')
    text = models.CharField(max_length=200, verbose_name=u'توضیح کوتاه در مورد دسته بندی', default="")
    img = models.ImageField(default='images/gallery/defaults.jpg', upload_to='images/category/', verbose_name=u'تصویر دسته بندی')
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.get_name_display()

    class Meta:
        ordering = ['name']
        verbose_name = u'دسته بندی محصولات'
        verbose_name_plural = u'دسته بندی محصولات'

# #******************End of Product Category ********************


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, verbose_name=u'دسته بندی محصولات')
    name = models.CharField(max_length=100, verbose_name=u'نام محصول')
    model = models.CharField(max_length=100, verbose_name=u'مدل محصول')
    specification = models.TextField(verbose_name=u'مشخصات', blank=True, null=True)
    price = models.IntegerField(default=0, verbose_name=u'قیمت مدل')
    description = models.TextField(verbose_name=u'توضیحات', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'"{0}" "{1}"'.format(self.name, self.model)

    class Meta:
        verbose_name = u'محصولات'
        verbose_name_plural = u'محصولات'

# #******************End of Product ********************


class ProductImage(models.Model):
    product = models.ForeignKey(Product, verbose_name=u'محصول', related_name='images')
    small_img = models.ImageField(upload_to='images/productImages/', verbose_name=u'ﺖﺻﻭیﺭ کﻭچک', help_text='size(370px * 294px)')
    big_img = models.ImageField(upload_to='images/productImages/', verbose_name=u'ﺖﺻﻭیﺭ بزرگ', help_text='size(570px * 453px)')
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.product.name

    class Meta:
        ordering = ['created_at']
        verbose_name = u'تصویر محصولات'
        verbose_name_plural = u'تصویر محصولات'
# #******************End of Product Image ********************


class Team(models.Model):
    name = models.CharField(max_length=500, verbose_name=u'نام')
    title = models.CharField(max_length=500, verbose_name=u'سمت')
    image = models.ImageField(blank=True, null=True, upload_to='images/team/', verbose_name=u'تصویر',
                              help_text='size(260*311)')
    priority = models.IntegerField(default=1, verbose_name="ترتیب چیدمان")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'تیم فنی'
        verbose_name_plural = u'تیم فنی'
