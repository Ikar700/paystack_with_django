from django.urls import path
from .views import PaymentInitView

app_name = 'payment' 

urlpatterns = [
    path('', PaymentInitView.as_view(), name='create')
]