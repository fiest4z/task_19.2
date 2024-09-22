from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView

from catalog.models import Product


# Create your views here.

class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')


# class ContactsTemplateView(TemplateView):
#     template_name = "templates/catalog/contacts.html"
#
#     def post(self, request):
#         if request.method == 'POST':
#             name = request.POST.get('name')
#             phone = request.POST.get('phone')
#             message = request.POST.get('message')
#             print(f'{name} ({phone}): {message}')
#         return render(request, 'catalog/contacts.html')
