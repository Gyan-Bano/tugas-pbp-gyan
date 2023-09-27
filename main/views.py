from django.shortcuts import redirect, render
from main.forms import ProductForm, StockUpdateForm
from main.models import Product
from django.db.models import Sum  # Import the Sum function from django.db.models
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    products = Product.objects.filter(user=request.user)
    total_stock = products.aggregate(total_stock=Sum('amount'))['total_stock'] or 0  # Calculate total stock

    context = {
        'app_name':'LibraLogia',
        'name': request.user.username,
        'class': 'PBP E', 
        'products': products,
        'total_stock': total_stock,  # Pass total_stock to the template
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, 'main.html', context)

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect('main:show_main')  
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

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/login')
def increase_stock(request, product_id):
    if request.method == 'POST':
        product = Product.objects.get(id=product_id, user=request.user)
        stock_update_form = StockUpdateForm(request.POST)
        if stock_update_form.is_valid() and stock_update_form.cleaned_data['action'] == 'increase':
            product.amount += 1
            product.save()
    return redirect('main:show_main')

@login_required(login_url='/login')
def decrease_stock(request, product_id):
    if request.method == 'POST':
        product = Product.objects.get(id=product_id, user=request.user)
        stock_update_form = StockUpdateForm(request.POST)
        if stock_update_form.is_valid() and stock_update_form.cleaned_data['action'] == 'decrease' and product.amount > 1:
            product.amount -= 1
            product.save()
    return redirect('main:show_main')

@login_required(login_url='/login')
def delete_product(request, product_id):
    if request.method == 'POST' and request.POST.get('action') == 'delete':
        try:
            product = Product.objects.get(id=product_id, user=request.user)
            product.delete()
        except Product.DoesNotExist:
            pass  # Product doesn't exist, no action required

    return redirect('main:show_main')