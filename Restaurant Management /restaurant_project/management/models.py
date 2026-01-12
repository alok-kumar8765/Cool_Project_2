from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal


class Category(models.Model):
    """
    Example:
    STARTER, MAIN COURSE, BEVERAGE, DESSERT
    """
    name = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    """
    Example:
    Pizza, Tea, Nacho Fries
    """
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="items"
    )
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    #half_plate_price = models.DecimalField(max_digits=8, decimal_places=2)
    #full_plate_price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(blank=True,null=True)
    image = models.ImageField(
        upload_to='menu_items/',
        blank=True,
        null=True
    )  # ✅ NEW
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ["category", "name"]
        unique_together = ("category", "name")

    def __str__(self):
        return f"{self.name} ({self.category.name})"


class Order(models.Model):
    order_number = models.CharField(max_length=20, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    SERVICE_PERCENT = 5
    TAX_PERCENT = 10

    def subtotal(self):
        return sum(item.cost() for item in self.items.all())

    def service_charge(self):
        return self.subtotal() * (Decimal(self.SERVICE_PERCENT) / Decimal('100'))


    def tax_charge(self):
        return self.subtotal() * (Decimal(self.TAX_PERCENT) / Decimal('100'))


    #def total_cost(self):
        #return round(
        #    self.subtotal() + self.service_charge() + self.tax_charge(),
        #    2
    #    )
    def total_cost(self):
        return (
        self.subtotal()
        + self.service_charge()
        + self.tax_charge()
    ).quantize(Decimal('0.01'))

    def __str__(self):
        return f"Order {self.order_number}"


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="items"
    )
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def cost(self):
        return self.quantity * self.item.price

    def __str__(self):
        return f"{self.item.name} x {self.quantity}"
