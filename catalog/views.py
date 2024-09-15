from django.shortcuts import render, get_object_or_404

from catalog.models import Product


# Create your views here.

def home(request):
    product_list = Product.objects.all()
    context = {"product_list": product_list}
    return render(request, 'product_list.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        message = request.POST['message']
        print(f'{name} {phone} {message}')
    return render(request, 'contacts.html')

def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, 'product_details.html', context)