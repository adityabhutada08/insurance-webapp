from django.shortcuts import render
from . forms import CustomerForm, FamilyMemberForm
# from django.views.decorators.csrf import csrf_exempt
# @csrf_exempt


# Create your views here.
def add_customer(request):
    form = CustomerForm()
    return render(request, 'customers/add_customer.html', {'form': form})

def add_family_member(request):
    form = FamilyMemberForm()
    return render(request, 'customers/add_family_member.html', {'form': form})
