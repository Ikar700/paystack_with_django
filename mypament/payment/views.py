from django.shortcuts import redirect,render
from django.contrib import messages
from django.urls import reverse
from django.views import View 
from .forms import PaymentInitForm


class PaymentInitView(View):
    def get(self, request):
        form = PaymentInitForm
        context = {
            'form' : form
        }
        return render (request, 'payment/create.html', context)
    
    def post(self, request):
        form = PaymentInitForm
        
        if form.is_valid():
            payment = form.save(commit=False)
            payment.save()

            request.session['payment_id'] = payment.id

            messages.success(request, "Payment Initialized Successfully")
            context = {
                'form': form
            }
            return redirect(request, 'payment/create.html', context)

