from django.shortcuts import render

from catalog.models import Product


def menu(request):
    return render(request, 'catalog/menu.html')

def dop(request):
    # context = {
    #     'object_list': Product.objects.all(),
    #     'title': 'Наши товары'
    # }
    return render(request, 'catalog/dop.html')

def testik(request):
    context = {
        'object_list': Product.objects.all()[:3]
    }
    return render(request, 'catalog/testik.html',context)
