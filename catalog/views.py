from django.shortcuts import render

from catalog.models import Product


def one(request,pk):
    product = Product.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(id=pk),
        'title': f'{Product.name}'
    }
    return render(request, 'catalog/one.html', context)

def dop(request):
    # context = {
    #     'object_list': Product.objects.all(),
    #     'title': 'Наши товары'
    # }
    return render(request, 'catalog/dop.html')

def testik(request):

    context = {
        'object_list': Product.objects.all(),
    }
    return render(request, 'catalog/testik.html',context)
#
def menu(request,pk):
    product = Product.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(category_id=pk),
        'title': f'{product.name}'
    }
    return render(request, 'catalog/one.html', context)