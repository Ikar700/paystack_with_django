import requests, json
from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect,render, get_object_or_404
from django.urls import reverse
from django.views import View
from .forms import PaymentInitForm
from .models import Payment



api_key = settings.PAYSTACK_SECRET_KEY
url = settings.PAYSTACK_INITIALIZE_PAYMENT_URL

class PaymentInitView(View):
    
    def get(self, request):
        form = PaymentInitForm()
        context = {
            'form' : form
        }
        return render (request, 'payment/create.html', context)
    
    def post(self, request):
        form = PaymentInitForm(request.POST)
        
        if form.is_valid():
            payment = form.save(commit=False)
            payment.save()

            request.session['payment_id'] = payment.id

            messages.success(request, "Payment Initialized Successfully")
            return redirect(reverse('payment:process'))
        
        context = {
            'form': form
        }   
        return redirect(request, 'payment/create.html', context)

    def payment_process(self, request):
        form = PaymentInitForm(self.request.POST)

        payment_id = self.request.session.get('payment_id', None)
        payment = get_object_or_404(Payment, payment_id)

        amount = payment.get_amount()

        success_url = request.build_absolute_url(
            reverse('payment:process')
        )
        
        cancel_url = request.build_absolute_url(
            reverse('payment:cancelled')
        )

        metadata = json.dumps(
            {"payment_id":payment_id,
             "cancel_action":cancel_url
             }
        )

        session_data = {
            'email' : payment.email,
            'amount' : int(amount),
            'callback_url' : success_url,
            'metadata' : metadata
        }
        