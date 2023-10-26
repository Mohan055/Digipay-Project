from django.shortcuts import render,redirect
from accounts.forms import user_form
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def sign_up(request):
    if request.method == "POST":
        form = user_form(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Hey {username}, your account was created successfully.")
    else:
        form = user_form()
    return render(request,"account/sign-up.html",{'form':form})

def sign_in(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # try:
            # user = User.objects.get(email=email)
        user = authenticate(username=username, password=password)
        print(user)
        if user: # if there is a user
            login(request, user)
            messages.success(request, "You are logged.")
            return redirect('bankaccounts:account')
        else:
            messages.warning(request, "Username or password does not exist")
            return redirect("accounts:sign_in")
        # except:
        #     messages.warning(request, "User does not exist")
    return render(request,"account/sign-in.html")


