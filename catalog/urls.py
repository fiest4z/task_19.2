from django.urls import path

from catalog.apps import NewappConfig
from catalog.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = NewappConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('catalog/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('catalog/create/', ProductCreateView.as_view(), name='product_create'),
    path('catalog/edit/<int:pk>/', ProductUpdateView.as_view(), name='product_edit'),
    path('catalog/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete')

]
