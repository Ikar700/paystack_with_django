from django.db import models

# Create your models here.
class Payment(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=20)
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50)
    email = models.EmailField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paystack_ref = models.CharField(max_length=15, blank=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'Payment {self.id}'

    def get_amount(self):
        return self.amount