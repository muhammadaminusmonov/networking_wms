from django.shortcuts import render
from sale.models import Sale
from django.utils.dateformat import DateFormat
import json

def dashboard(request):
    sales = Sale.objects.order_by('date')

    # Format date labels and collect amounts
    labels = [DateFormat(sale.date).format('M j') for sale in sales]  # Example: Jan 5
    data = [sale.amount for sale in sales]

    ctx = {
        'labels': json.dumps(labels),
        'data': json.dumps(data),
    }
    return render(request, 'dashboard.html', ctx)