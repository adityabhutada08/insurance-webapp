from django.shortcuts import render, redirect
from . forms import RegistrationForm
from . models import Account
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import authenticate
#exempt csrf token
# from django.views.decorators.csrf import csrf_exempt
# @csrf_exempt

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split("@")[0]
            user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
            user.phone_number = phone_number

            user.is_active = True  # Automatically activate the user upon registration
            user.save()

            return redirect('login')
    else:
        form = RegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/register.html', context)


# @csrf_exempt
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print(f"Attempting to authenticate user with email: {email}")

        user = authenticate(email=email, password=password)
        print(f"User authenticated: {user}")

        if user is not None:
            auth.login(request, user)
            messages.success(request, "You have successfully logged in!!")
            return redirect('home')
        else:
            messages.error(request, "Invalid email or password! Try again with valid credentials")
            return redirect('login')

    return render(request, 'accounts/login.html')


@login_required(login_url= 'login')  # Ensures that the user must be logged in to access this view
def logout(request):
    auth.logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('login')

