from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import Http404
from .models import Product

from .forms import ProductForm


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "products/product_list.html", context)


def product_create_view(request):
    form = ProductForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        "form" : form
    }
    return render(request, "products/product_create.html", context)


def product_detail_view(request, id):
    obj = get_object_or_404(Product, id=id)
    context = {
        "object" : obj
    }
    return render(request, "products/product_detail.html", context)


def product_update_view(request, id):
    obj = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, request.FILES, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)


def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('../../')
    context = {
        "object" : obj
    }
    return render (request, "products/product_delete.html", context)

def product_category_view(request,categoryId):
    queryset = 0
    if(categoryId != 0):
        queryset = Product.objects.filter(categoryId=categoryId)
    else:
        queryset = Product.objects.all()

    context = {
        "object_list": queryset,
        "categoryID": categoryId
    }
    return render(request, "products/product_list.html", context)
