from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm

def product(request):
    products = Product.objects.all()
    ctx = {
        'products': products
    }
    return render(request, 'product.html', ctx)

def product_add(request):
    form = ProductForm(request.POST or None)
    print(request.POST)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('product')
    ctx = {'form': form, 'title': 'Add Product'}
    return render(request, 'new_update.html', ctx)

def product_edit(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    form = ProductForm(request.POST or None, instance=product)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('product')
    ctx = {'form': form, 'title': 'Edit Product'}
    return render(request, 'new_update.html', ctx)

def product_delete(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    return redirect('product')