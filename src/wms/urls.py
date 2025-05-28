"""
URL configuration for wms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import dashboard
from product.views import product, product_add, product_edit, product_delete
from sale.views import sale, sale_add, sale_edit, sale_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),
    path('product/', product, name='product'),
    path('product/add/', product_add, name='product_add'),
    path('product/<int:product_id>/', product_edit, name='product_edit'),
    path('product/<int:product_id>/delete/', product_delete, name='product_delete'),
    path('sale/', sale, name='sale'),
    path('sale/add/', sale_add, name='sale_add'),
    path('sale/<int:sale_id>/', sale_edit, name='sale_edit'),
    path('sale/<int:sale_id>/delete/', sale_delete, name='sale_delete'),
]
