from django.urls import path
from catalog.apps import NewappConfig
from catalog.views import home, contacts, product_details

app_name = NewappConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('catalog/<int:pk>', product_details, name='product_details')

]
