from django.urls import path
from .views import PaymentInitView, PaymentProcessView, payment_success, payment_canceled

app_name = 'payment' 

urlpatterns = [
    path('', PaymentInitView.as_view(), name='create'),
    path('process/', PaymentProcessView.as_view(), name='process'),
    path('success/', payment_success, name='success'),
    path('canceled/', payment_canceled, name='canceled'),
]