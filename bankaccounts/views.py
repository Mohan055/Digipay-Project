from django.shortcuts import render,redirect
from bankaccounts.forms import KYC_form
from bankaccounts.models import Account,KYC
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from transactions.models import Transaction, CreditCard
from transactions.forms import CreditCardForm

@login_required(login_url="sign_in")
def account(request):
    kyc = KYC.objects.get(user=request.user)
    account = Account.objects.get(user=request.user)
    context= {
        'kyc':kyc,
        'account':account
    }
    return render(request,'account/account.html',context)


def KYC_reg(request):
    user = request.user
    account = Account.objects.get(user=user)
    
    try:
        kyc = KYC.objects.get(user=user)
    except:
        kyc = None

    if request.method == 'POST':
        form = KYC_form(request.POST,request.FILES,instance=kyc)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = user
            new_form.account = account
            new_form.save()
            messages.success(request,"KYC Form submitted successfully, In review now")
            return redirect("kyc")

    else:
        form = KYC_form(instance=kyc)
    context = {
        "account" : account,
        "form" : form ,
        "kyc" : kyc,
    }
    return render(request, 'KYC_form.html', context)

def KYC_logout(request):
    logout(request)
    return redirect('accounts:sign_in')

def dashboard(request):
    user=request.user
    account = Account.objects.get(user=user)
    transaction = Transaction.objects.all()
    credit_card = CreditCard.objects.all()
    form = CreditCardForm()
    if request.method == 'POST':
        form = CreditCardForm(request.POST)
        if form.is_valid():
            form.save()
    context = {
        'account':account,
        'transaction':transaction,
        'form':form,
        'credit_card':credit_card,
    }
    return render(request,'account/dashboard.html',context)

def add_card(request):
            
    return render(request,'account/add_card.html')