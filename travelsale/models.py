from django.db import models
from django.db.models import UniqueConstraint
from django.contrib.auth.models import User
from django.urls import reverse
from decimal import Decimal


class Paymethod(models.Model):
    paymethod_id = models.AutoField(primary_key=True)
    payment_method = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f'{self.payment_method}'

    class Meta:
        ordering = ['payment_method']


class Type(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f'{self.type_name}'

    def get_absolute_url(self):
        return reverse('travelsale_type_detail_urlpattern',
                        kwargs={'pk': self.pk}
                        )

    def get_update_url(self):
        return reverse('travelsale_type_update_urlpattern',
                        kwargs={'pk': self.pk}
                        )

    def get_delete_url(self):
        return reverse('travelsale_type_delete_urlpattern',
                        kwargs={'pk': self.pk}
                        )

    class Meta:
        ordering = ['type_name']


class Destination(models.Model):
    destination_id = models.AutoField(primary_key=True)
    destination_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f'{self.destination_name}'

    def get_absolute_url(self):
        return reverse('travelsale_destination_detail_urlpattern',
                        kwargs={'pk': self.pk}
                        )

    def get_update_url(self):
        return reverse('travelsale_destination_update_urlpattern',
                        kwargs={'pk': self.pk}
                        )

    def get_delete_url(self):
        return reverse('travelsale_destination_delete_urlpattern',
                        kwargs={'pk': self.pk}
                        )

    class Meta:
        ordering = ['destination_name']


class Travelproduct(models.Model):
    travelproduct_id = models.AutoField(primary_key=True)
    travelproduct_name = models.CharField(max_length=300)
    type = models.ForeignKey(Type, related_name='travelproducts', on_delete=models.PROTECT)
    destination = models.ForeignKey(Destination, related_name='travelproducts', on_delete=models.PROTECT)
    price = models.DecimalField(default = Decimal('0'), decimal_places = 2, max_digits = 15)
    discount = models.DecimalField(default = Decimal('0.00'), decimal_places = 2, max_digits = 3)
    duration = models.IntegerField()
    description = models.CharField(max_length=5000)

    def __str__(self):
        return f'{self.travelproduct_name} - {self.type} - {self.destination}'

    def get_absolute_url(self):
        return reverse('travelsale_travelproduct_detail_urlpattern',
                        kwargs={'pk': self.pk}
                        )

    def get_update_url(self):
        return reverse('travelsale_travelproduct_update_urlpattern',
                        kwargs={'pk': self.pk}
                        )

    def get_delete_url(self):
        return reverse('travelsale_travelproduct_delete_urlpattern',
                        kwargs={'pk': self.pk}
                        )

    class Meta:
        ordering = ['travelproduct_name', 'type', 'destination']
        constraints = [
            UniqueConstraint(fields=['travelproduct_name', 'type', 'destination'], name='unique_travelproduct')
        ]


class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    job_position = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.last_name}, {self.first_name} ({self.job_position})'

    def get_absolute_url(self):
        return reverse('travelsale_staff_detail_urlpattern',
                        kwargs={'pk': self.pk}
                        )

    def get_update_url(self):
        return reverse('travelsale_staff_update_urlpattern',
                        kwargs={'pk': self.pk}
                        )

    def get_delete_url(self):
        return reverse('travelsale_staff_delete_urlpattern',
                        kwargs={'pk': self.pk}
                        )

    class Meta:
        ordering = ['last_name', 'first_name', 'job_position']
        constraints = [
            UniqueConstraint(fields=['last_name', 'first_name', 'job_position'],
                             name='staff')
        ]


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

    def get_absolute_url(self):
        return reverse('travelsale_customer_detail_urlpattern',
                        kwargs={'pk': self.pk}
                        )

    def get_update_url(self):
        return reverse('travelsale_customer_update_urlpattern',
                        kwargs={'pk': self.pk}
                        )

    def get_delete_url(self):
        return reverse('travelsale_customer_delete_urlpattern',
                        kwargs={'pk': self.pk}
                        )

    class Meta:
        ordering = ['last_name', 'first_name']


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    travelproduct = models.ForeignKey(Travelproduct, related_name='orders', on_delete=models.PROTECT)
    staff = models.ForeignKey(Staff, related_name='orders', on_delete=models.PROTECT)
    start_date = models.DateField()

    def __str__(self):
        return f'{self.order_id} - {self.travelproduct.travelproduct_name} - {self.staff}'

    def get_absolute_url(self):
        return reverse('travelsale_order_detail_urlpattern',
                        kwargs={'pk': self.pk}
                        )

    def get_update_url(self):
        return reverse('travelsale_order_update_urlpattern',
                        kwargs={'pk': self.pk}
                        )

    def get_delete_url(self):
        return reverse('travelsale_order_delete_urlpattern',
                        kwargs={'pk': self.pk}
                        )

    class Meta:
        ordering = ['order_id', 'travelproduct', 'staff']
        constraints = [
            UniqueConstraint(fields=['travelproduct', 'staff', 'order_id'],
                             name='unique_order')
        ]


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, related_name='payments', on_delete=models.PROTECT, unique=True)
    customer = models.ForeignKey(Customer, related_name='payments', on_delete=models.PROTECT)
    paymethod = models.ForeignKey(Paymethod, related_name='payments', on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.order} - {self.customer}'

    def get_absolute_url(self):
        return reverse('travelsale_payment_detail_urlpattern',
                        kwargs={'pk': self.pk}
                        )

    def get_update_url(self):
        return reverse('travelsale_payment_update_urlpattern',
                        kwargs={'pk': self.pk}
                        )

    def get_delete_url(self):
        return reverse('travelsale_payment_delete_urlpattern',
                        kwargs={'pk': self.pk}
                        )

    class Meta:
        ordering = ['order', 'customer']
        constraints = [
            UniqueConstraint(fields=['order', 'customer'], name='unique_payment')
        ]

