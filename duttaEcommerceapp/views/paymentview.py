from django.shortcuts import render, redirect
from duttaEcommerceapp.forms.paymentform import PaymentForm

def proceed_to_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment_success')  # Redirect to a success page
    else:
        form = PaymentForm()

    return render(request, 'proceed_to_payment.html', {'form': form})

def payment_success(request):
    return render(request, 'payment_success.html')

