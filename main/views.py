from django.shortcuts import redirect, render
from main.forms import ProductForm
from main.models import Product
from django.db.models import Sum  # Import the Sum function from django.db.models
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_main(request):
    products = Product.objects.all()
    total_stock = products.aggregate(total_stock=Sum('amount'))['total_stock'] or 0  # Calculate total stock

    context = {
        'app_name':'LibraLogia',
        'name': 'Gyanamurti Adhikara Bano', 
        'class': 'PBP E', 
        'products': products,
        'total_stock': total_stock,  # Pass total_stock to the template
    }

    return render(request, 'main.html', context)

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Redirect to a success page or any other desired action
            return redirect('main:show_main')  # Assuming 'show_main' is the URL name for your main page
    else:
        form = ProductForm()
    
    context = {'form': form}
    return render(request, 'create_product.html', context)

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
