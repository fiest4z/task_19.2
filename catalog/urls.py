from django.urls import path
from catalog.apps import NewappConfig
from catalog.views import ProductListView, ProductDetailView

app_name = NewappConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('catalog/<int:pk>', ProductDetailView.as_view(), name='product_detail')

]
