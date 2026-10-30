from django.conf import settings
from django.db import models

from menu.models import Dish


class Order(models.Model):
    class Status(models.TextChoices):
        PENDING = 'pending', 'Chờ xử lý'
        PREPARING = 'preparing', 'Đang làm'
        DELIVERING = 'delivering', 'Đang giao'
        DONE = 'done', 'Hoàn tất'
        CANCELLED = 'cancelled', 'Đã hủy'

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='orders')
    full_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Đơn #{self.pk}'

    @property
    def total(self):
        return sum(item.subtotal for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    dish = models.ForeignKey(Dish, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)
    # Giá chốt lúc đặt, để đổi giá món sau này không làm sai đơn cũ.
    unit_price = models.DecimalField(max_digits=10, decimal_places=0)

    def __str__(self):
        return f'{self.quantity} x {self.dish}'

    @property
    def subtotal(self):
        return self.quantity * self.unit_price
