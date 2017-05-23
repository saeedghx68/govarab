# coding=utf-8
from django.shortcuts import render, render_to_response
from config import settings
from myapp.models import *
# from django.utils.translation import activate

# activate('fa-ir')


def home(request):
    c = {}
    c['LANGUAGES'] = settings.LANGUAGES
    c['SELECTEDLANG'] = request.LANGUAGE_CODE
    try:
        c['productCategory'] = ProductCategory.objects.all()
        c['products'] = Product.objects.all()
        c['FAQs'] = FAQ.objects.all()
        c['gallery'] = Gallery.objects.all()
        c['team'] = Team.objects.all()
    except:
        print (u'داده ها وارد نشده!')
    return render_to_response('index.html', c)

