from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from . models import Product
from cart.cart import Cart

def index(request):
    product = {
        'product':Product .objects.all()
    }
    return render(request, 'index.html',product)

def cart(request):
    return render(request,'cart.html')
def login(request):
    return render(request,'login.html')

def blogsingle(request):
    return render(request,'blog-single.html')
def blog(request):
    return render(request,'blog.html')

@login_required
def checkout(request):
    return render(request,'checkout.html')
def contact(request):
    return render(request,'contact-us.html')

def product(request, id):
    product = {
        'product':Product .objects.get(id=id)
    }
    return render(request, 'product.html',product)

def shop(request):
    return render(request,'shop.html')

def register(request):
    form = UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('index')
    return render(request,'register.html',{'form':form})



@login_required
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("index")


# @login_required(login_url="/users/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart")


# @login_required(login_url="/users/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart")


# @login_required(login_url="/users/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart")


# @login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart")


@login_required
def cart_detail(request,id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("product")
    # return render(request, 'cart/cart_detail.html')
