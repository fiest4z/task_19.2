from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        message = request.POST['message']
        print(f'{name} {phone} {message}')
    return render(request, 'contacts.html')
