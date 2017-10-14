from django.db import models

from users.models import UserModel
from workers.models import Worker


class OrderType(models.Model):
    order_type_name = models.CharField(max_length=100)

    def __str__(self):
        return self.order_type_name


class Order(models.Model):
    statuses = (
        ('NE', 'New'),
        ('AC', 'Accepted'),
        ('AG', 'Assigned'),
        ('ST', 'Started'),
        ('IP', 'In Progress'),
        ('DN', 'Done'),
        ('IV', 'Invoiced'),
        ('PD', 'Paid')
    )
    order_date = models.DateTimeField()
    order_status = models.CharField(max_length=2, choices=statuses)
    order_description = models.TextField()
    order_type = models.ForeignKey(OrderType, on_delete=models.SET_NULL, null=True)
    assigned_to = models.ForeignKey(Worker, on_delete=models.SET_NULL, null=True)
    created_by = models.ForeignKey(UserModel, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.order_status
