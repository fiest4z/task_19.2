from django.urls import path
from catalog.apps import NewappConfig
from catalog.views import ProductListView, ProductDetailView, contacts

app_name = NewappConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('contacts/', contacts, name='contacts'),
    path('catalog/<int:pk>', ProductDetailView.as_view(), name='product_detail')

]
