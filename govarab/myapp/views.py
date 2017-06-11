# coding=utf-8
from django.shortcuts import render, render_to_response
from django.utils.translation import ugettext_lazy as _
from config import settings
from myapp.models import *
from django.utils import translation
user_language = 'fa'
translation.activate(user_language)


def home(request):
    request.session[translation.LANGUAGE_SESSION_KEY] = user_language
    c = {}
    c['LANGUAGES'] = settings.LANGUAGES
    c['SELECTEDLANG'] = request.LANGUAGE_CODE
    try:
        c['slidesImages'] = SlidesImages.objects.all()
        c['productCategory'] = ProductCategory.objects.all()
        c['products'] = Product.objects.all()
        c['FAQs'] = FAQ.objects.all()
        c['gallery'] = Gallery.objects.all()
        c['articles'] = Article.objects.all()[0:3]
        c['team'] = Team.objects.all()
        c['slogan'] = Slogan.objects.all().order_by('priority')
        c['resellers'] = Dealership.objects.filter(type='1')
        c['representatives'] = Dealership.objects.filter(type='2')
        c['catalog'] = Catalog.objects.all()[0]
    except:
        print (u'داده ها وارد نشده!')
    return render_to_response('index.html', c)


def product_details(request, product_id):
    request.session[translation.LANGUAGE_SESSION_KEY] = user_language
    c = {}
    c['LANGUAGES'] = settings.LANGUAGES
    c['SELECTEDLANG'] = request.LANGUAGE_CODE
    try:
        c['product'] = Product.objects.get(pk=product_id)
    except Exception as e:
        print e
        c['product'] = u'محصولی با این id وجود ندارد!'
    try:
        c['products'] = Product.objects.all()
    except:
        c['products'] = u'محصولی وارد نشده!'
    try:
        c['productCategory'] = ProductCategory.objects.all()
    except:
        c['productCategory'] = u'دسته بندی وجود ندارد!'
    try:
        c['catalog'] = Catalog.objects.all()[0]
    except:
        c['catalog'] = u'کاتالوگ اضافه نشده'

    return render_to_response('product_details.html', c)


def article_single(request, article_id):
    request.session[translation.LANGUAGE_SESSION_KEY] = user_language
    c = {}
    c['LANGUAGES'] = settings.LANGUAGES
    c['SELECTEDLANG'] = request.LANGUAGE_CODE
    try:
        c['article'] = Article.objects.get(pk=article_id)
    except Exception as e:
        print e
        c['article'] = u'مقاله ای با این id وجود ندارد!'
    try:
        c['articles'] = Article.objects.all()
    except:
        c['articles'] = u'مقاله ای وارد نشده!'
    try:
        c['catalog'] = Catalog.objects.all()[0]
    except:
        c['catalog'] = u'کاتالوگ اضافه نشده'

    return render_to_response('article_single.html', c)


def articles(request):
    request.session[translation.LANGUAGE_SESSION_KEY] = user_language
    c = {}
    c['LANGUAGES'] = settings.LANGUAGES
    c['SELECTEDLANG'] = request.LANGUAGE_CODE
    try:
        c['articles'] = Article.objects.all()
    except:
        c['articles'] = u'مقاله ای وارد نشده!'
    try:
        c['catalog'] = Catalog.objects.all()[0]
    except:
        c['catalog'] = u'کاتالوگ اضافه نشده'

    return render_to_response('articles.html', c)
