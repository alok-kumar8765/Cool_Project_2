from django.shortcuts import render, redirect, get_object_or_404
from .models import MenuItem, Order, OrderItem
from .forms import OrderItemFormSet, MenuItemForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import random
from django.http import HttpResponse
from django.template.loader import render_to_string
import pdfkit  # pip install pdfkit and install wkhtmltopdf
from django.db.models import Q
from django.contrib.auth.decorators import user_passes_test


@login_required
def all_orders(request):
    query = request.GET.get('q')
    orders = Order.objects.all().order_by('-created_at')  # Latest first

    if query:
        orders = orders.filter(order_number__icontains=query)

    return render(request, 'management/all_orders.html', {
        'orders': orders,
        'query': query or ''
    })

@login_required
def dashboard(request):
    menu = MenuItem.objects.filter(available=True)
    return render(request, 'management/dashboard.html', {'menu': menu})

@login_required
def create_order(request):
    # Generate order instance with Order ID immediately
    if request.method == 'POST':
        order = Order.objects.create(
            user=request.user,
            order_number=request.POST.get('order_number')
        )
        formset = OrderItemFormSet(request.POST, instance=order)

        if formset.is_valid():
            formset.save()
            messages.success(request, f"Order {order.order_number} saved successfully!")
            return redirect('order_receipt', order_id=order.id)
    else:
        # Generate random Order ID before saving
        order_number = f"ORD{random.randint(1000,9999)}"
        order = Order(user=request.user, order_number=order_number)
        formset = OrderItemFormSet(instance=order)

    return render(request, 'management/create_order.html', {
        'formset': formset,
        'order_number': order.order_number
    })


@login_required
def order_receipt(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    # If PDF requested
    if request.GET.get('pdf') == '1':
        html = render_to_string('management/order_receipt_pdf.html', {'order': order})
        pdf = pdfkit.from_string(html, False)
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="Receipt_{order.order_number}.pdf"'
        return response

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

# Only superusers can delete orders
@user_passes_test(lambda u: u.is_superuser)
@login_required
def delete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.delete()
    messages.success(request, f"Order {order.order_number} deleted successfully!")
    return redirect('all_orders')