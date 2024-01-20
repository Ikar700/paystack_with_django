from django.urls import path
from .views import PaymentInitView

urlpatterns = [
    path('', PaymentInitView.as_view(), name='create')
]