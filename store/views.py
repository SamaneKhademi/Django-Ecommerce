from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm

def category(request, foo):
    # Replace hyphens with spaces
    foo = foo.replace("-", " ")
    # Greb the category from the url
    try:
        # Look up the category
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(request, 'category.html', {"products": products, 'category': category})
    except:
        messages.success(request, 'این دسته بندی وجود ندارد')
        return redirect('home')

def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {'product': product})

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def about(request):
    return render(request, 'about.html', {})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'با موفقیت وارد شدید.')
            return redirect('home')
        else:
            messages.error(request, 'مشکلی در ورود به صفحه کاربری وجود دارد! لطفاِ دوباره امتحان کنید.')
            return redirect('login')
    else:
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, 'با موفقیت خارج شدید.')
    return redirect('home')

def register_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # Log in user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'ثبت نام با موفقیت انجام شد. به صفحه کاربری وارد شدید.')
            return redirect('home')
        else:
            messages.success(request, 'مشکلی در ثبت نام وجود دارد! لطفا دوباره امتحان کنید.')
            return redirect('register')
    else:
        return render(request, 'register.html', {'form': form})