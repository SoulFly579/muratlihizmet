from django.shortcuts import render
from home.models import Category,Haberler,Setting, Image
from django.core.mail import send_mail
from django.db import models
from django.contrib.auth.models import User
from django.core.paginator import Paginator


def index(request):
    setting = Setting.objects.get(pk=1)
    haber = Haberler.objects.all()
    category = Category.objects.all()
    sliderdata = Haberler.objects.all()[:4]
    paginator = Paginator(haber,12)
    page = request.GET.get('page')
    haber = paginator.get_page(page)
    context = {
        'haber':haber,
        'sliderdata':sliderdata,
        'category':category,
        'setting':setting
    }
    return render(request, 'index.html', context)

def haber(request,id,slug):
    setting = Setting.objects.get(pk=1)
    haber = Haberler.objects.get(id=id)
    category = Category.objects.all()
    context = {
        'haber':haber,
        'category':category,
        'setting':setting
    }
    return render(request, 'post.html', context)

def category_haber(request,id,slug):
    setting = Setting.objects.get(pk=1)
    category_filter = Category.objects.filter(pk=id)
    haber_filter = Haberler.objects.filter(category_id=id)
    category = Category.objects.all()
    context = {
        'page':'filter',
        'category':category,
        'haber':haber_filter,
        'setting':setting
    }
    return render(request, 'index.html', context)

def iletisim(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {
        'page':'filter',
        'category':category,
        'setting':setting
    }
    return render(request, 'iletisim.html', context)

def yazar(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    user = User.objects.all()
    image = Image.objects.all()
    context = {
        'image':image,
        'user':user,
        'page':'filter',
        'category':category,
        'setting':setting
    }
    return render(request, 'yazar.html', context)

def kunye(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {
        'page':'filter',
        'category':category,
        'setting':setting
    }
    return render(request, 'kunye.html', context)
