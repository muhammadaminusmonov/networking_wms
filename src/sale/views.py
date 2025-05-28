from django.shortcuts import render, redirect, get_object_or_404
from .models import Sale
from .forms import SaleForm

def sale(request):
    sales = Sale.objects.all()
    ctx = {'sales': sales}
    return render(request, 'sale.html', ctx)

def sale_add(request):
    form = SaleForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('sale')
    ctx = {'form': form, 'title': 'Add Sale'}
    return render(request, 'new_update.html', ctx)

def sale_edit(request, sale_id):
    sale = get_object_or_404(Sale, pk=sale_id)
    form = SaleForm(request.POST or None, instance=sale)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('sale')
    ctx = {'form': form, 'title': 'Edit Sale'}
    return render(request, 'new_update.html', ctx)

def sale_delete(request, sale_id):
    sale = get_object_or_404(Sale, pk=sale_id)
    sale.delete()
    return redirect('sale')
