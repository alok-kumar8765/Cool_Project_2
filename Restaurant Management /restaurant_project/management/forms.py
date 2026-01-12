from django import forms
from .models import Order, OrderItem, MenuItem
from django.forms import inlineformset_factory

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['item', 'quantity']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['item'].widget.attrs.update({'class': 'item-select'})
        self.fields['quantity'].widget.attrs.update({'class': 'qty-input'})

OrderItemFormSet = inlineformset_factory(Order, OrderItem, form=OrderItemForm, extra=5, can_delete=True)

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['category','name', 'price', 'available']