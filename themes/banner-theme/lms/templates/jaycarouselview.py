from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


from home.models import Setting, ContactForm, ContactMessage
from product.models import Category, Product

def index(request):
    setting Setting.objects.get(pk=1)
    category = Category.objects.all()
    banner_slider = Product.Objects.all().order_by('-id')[:4]
    page="home"
    context = {
            'setting':setting,
            'page':page,
            'category':category,
            'banner_slider': banner_slider,
    }
    return render(request, 'index.html', context)
