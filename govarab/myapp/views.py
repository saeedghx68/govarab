# coding=utf-8
from django.shortcuts import render, render_to_response
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
        c['productCategory'] = ProductCategory.objects.all()
        c['products'] = Product.objects.all()
        c['FAQs'] = FAQ.objects.all()
        c['gallery'] = Gallery.objects.all()
        c['team'] = Team.objects.all()
        c['slogan'] = Slogan.objects.all().order_by('priority')
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

    return render_to_response('product_details.html', c)
