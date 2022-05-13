from django.shortcuts import render, redirect
from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    filter_ = request.GET.get('sort', 'name')
    if filter_ == 'min_price':
        phones = Phone.objects.all().order_by('price')
    elif filter_ == 'max_price':
        phones = Phone.objects.all().order_by('-price')
    else:
        phones = Phone.objects.all().order_by(filter_)
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
