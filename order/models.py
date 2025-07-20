from django.db import models
from django.contrib.auth.models import User
from store.models import Product

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="المستخدم")
    created_at = models.DateTimeField("تاريخ الطلب", auto_now_add=True)
    completed = models.BooleanField("تم التنفيذ؟", default=False)

    class Meta:
        verbose_name = "طلب"
        verbose_name_plural = "الطلبات"

    def __str__(self):
        return f"طلب رقم {self.id} - {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE, verbose_name="الطلب")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="المنتج")
    quantity = models.PositiveIntegerField("الكمية", default=1)

    class Meta:
        verbose_name = "عنصر طلب"
        verbose_name_plural = "عناصر الطلب"

    def __str__(self):
        return f"{self.quantity} × {self.product.name}"
