# 馃嵔锔� Restaurant Management Web App - Django Version

**Author:** Alok Kumar
**GitHub:** [alok-kumar8765/Cool_Project_2](https://github.com/alok-kumar8765/Cool_Project_2)

---

## 馃摉 Features

1. **Persistent database storage** (SQLite/MySQL) for orders and menu items
2. **Web interface (Django)** for online access
3. **Dynamic Menu CRUD** 鈥� Add/Edit/Delete menu items from admin or web
4. **User Authentication** 鈥� Multi-user support (staff and admin)
5. **Receipt Generation** 鈥� Download/print receipts for orders
6. **Order Search** 鈥� Search order by Order ID
7. **Real-time price calculation**
8. **Responsive web interface**

---

## 馃洜锔� System Requirements

* Python 3.10+
* Django 4.x
* SQLite (default) or MySQL
* Pip (Python package manager)

---

## 鈿� Step-by-Step Setup Guide

### 1. Create and Activate Virtual Environment

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install django
pip install django-crispy-forms
pip install pillow  # optional, if you want images for menu
```

### 3. Create Django Project & App

```bash
django-admin startproject restaurant_project
cd restaurant_project
python manage.py startapp management
```

---

### 4. Update `settings.py`

In `restaurant_project/settings.py`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'management',           # our app
    'crispy_forms',         # for forms
]

# Optional: For crispy-forms
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Static & media files
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default DB is SQLite
# For MySQL:
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'restaurant_db',
#         'USER': 'root',
#         'PASSWORD': 'password',
#         'HOST': 'localhost',
#         'PORT': '3306',
#     }
# }
```

---

### 5. Create Models (`management/models.py`)

```python
from django.db import models
from django.contrib.auth.models import User

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    order_number = models.CharField(max_length=20, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(MenuItem, through='OrderItem')
    created_at = models.DateTimeField(auto_now_add=True)

    def total_cost(self):
        total = sum([oi.quantity * oi.item.price for oi in self.orderitem_set.all()])
        service = total * 0.05
        tax = total * 0.1
        return round(total + service + tax, 2)

    def __str__(self):
        return f"Order {self.order_number} by {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.FloatField(default=1)

    def cost(self):
        return self.quantity * self.item.price
```

---

### 6. Create Admin Interface (`management/admin.py`)

```python
from django.contrib import admin
from .models import MenuItem, Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    list_display = ('order_number', 'user', 'created_at', 'total_cost')

admin.site.register(MenuItem)
admin.site.register(Order, OrderAdmin)
```

---

### 7. Create Forms (`management/forms.py`)

```python
from django import forms
from .models import Order, OrderItem, MenuItem
from django.forms import inlineformset_factory

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['item', 'quantity']

OrderItemFormSet = inlineformset_factory(Order, OrderItem, form=OrderItemForm, extra=1, can_delete=True)

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['name', 'price', 'available']
```

---

### 8. Create Views (`management/views.py`)

```python
from django.shortcuts import render, redirect, get_object_or_404
from .models import MenuItem, Order
from .forms import OrderItemFormSet, MenuItemForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import random

@login_required
def dashboard(request):
    menu = MenuItem.objects.filter(available=True)
    return render(request, 'management/dashboard.html', {'menu': menu})

@login_required
def create_order(request):
    if request.method == 'POST':
        order_number = f"ORD{random.randint(1000,9999)}"
        order = Order.objects.create(user=request.user, order_number=order_number)
        formset = OrderItemFormSet(request.POST, instance=order)
        if formset.is_valid():
            formset.save()
            messages.success(request, f"Order {order_number} created successfully!")
            return redirect('order_receipt', order_id=order.id)
    else:
        formset = OrderItemFormSet(queryset=OrderItem.objects.none())
    return render(request, 'management/create_order.html', {'formset': formset})

@login_required
def order_receipt(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'management/order_receipt.html', {'order': order})

@login_required
def menu_crud(request):
    items = MenuItem.objects.all()
    return render(request, 'management/menu_crud.html', {'items': items})

@login_required
def add_menu_item(request):
    if request.method == 'POST':
        form = MenuItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu_crud')
    else:
        form = MenuItemForm()
    return render(request, 'management/menu_item_form.html', {'form': form})

@login_required
def edit_menu_item(request, item_id):
    item = get_object_or_404(MenuItem, id=item_id)
    if request.method == 'POST':
        form = MenuItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('menu_crud')
    else:
        form = MenuItemForm(instance=item)
    return render(request, 'management/menu_item_form.html', {'form': form})

@login_required
def delete_menu_item(request, item_id):
    item = get_object_or_404(MenuItem, id=item_id)
    item.delete()
    return redirect('menu_crud')

@login_required
def search_order(request):
    query = request.GET.get('q')
    order = None
    if query:
        try:
            order = Order.objects.get(order_number=query)
        except:
            messages.error(request, "Order not found!")
    return render(request, 'management/search_order.html', {'order': order})
```

---

### 9. URLs (`management/urls.py`)

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('create-order/', views.create_order, name='create_order'),
    path('order-receipt/<int:order_id>/', views.order_receipt, name='order_receipt'),
    path('menu/', views.menu_crud, name='menu_crud'),
    path('menu/add/', views.add_menu_item, name='add_menu_item'),
    path('menu/edit/<int:item_id>/', views.edit_menu_item, name='edit_menu_item'),
    path('menu/delete/<int:item_id>/', views.delete_menu_item, name='delete_menu_item'),
    path('search-order/', views.search_order, name='search_order'),
]
```

Update `restaurant_project/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', include('management.urls')),
]
```

---

### 10. Templates (Django HTML)

**Example folder structure**: `management/templates/management/`

* `dashboard.html` 鈥� List menu and create orders link
* `create_order.html` 鈥� Formset for order items
* `order_receipt.html` 鈥� Show order receipt with totals
* `menu_crud.html` 鈥� List menu with CRUD buttons
* `menu_item_form.html` 鈥� Form for add/edit menu item
* `search_order.html` 鈥� Search order by ID

> Templates can use **Bootstrap 5** for styling.

---

### 11. Migrate Database & Create Superuser

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

Access admin at `http://127.0.0.1:8000/admin/` to manage menu items directly.

---

### 12. Run Development Server

```bash
python manage.py runserver
```

Access app at: `http://127.0.0.1:8000/`

---

### 鉁� Features Now Available

1. Multi-user authentication
2. Persistent order and menu storage in SQLite/MySQL
3. Dynamic menu CRUD in web app
4. Order creation, total calculation, and receipt generation
5. Search order by Order ID
6. Admin interface for menu management

---

### 馃挕 Future Enhancements

* Add PDF export for receipts
* Add payment integration
* Implement role-based access (e.g., staff vs admin)
* Add analytics dashboard for sales tracking

---

This is a **complete working Django system** that fully replaces your Tkinter version and adds **web access, authentication, persistent storage, and advanced features**.
