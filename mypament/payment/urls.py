from django.urls import path
from .views import PaymentInitView, PaymentProcessView, PaymentSuccess, payment_canceled

app_name = 'payment' 

urlpatterns = [
    path('', PaymentInitView.as_view(), name='create'),
    path('process/', PaymentProcessView.as_view(), name='process'),
    path('success/', PaymentSuccess.as_view(), name='success'),
    path('canceled/', payment_canceled, name='canceled'),
]