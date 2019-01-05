#Customer views

#Django
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from rest_framework import viewsets

#Forms
from .forms import UserForm

#Models
from .models import Customer

#Serializer
from .serializers import UserSerializer

def index(request):
    #return HttpResponse("Introduce customer data")

    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            customer = Customer()
            customer.first_Name = form.cleaned_data['first_name']
            customer.last_Name = form.cleaned_data['last_name']
            customer.streetAdd = form.cleaned_data['address']
            customer.city = form.cleaned_data['city']
            customer.state = form.cleaned_data['state']
            customer.zipNumber = form.cleaned_data['zip_number']

            customer.save()

            return HttpResponseRedirect('/customer/data')

    else:
        form = UserForm()

    return render(request,'customer.html',{'form':form})

def data(request):
    return render(request,'data.html')

class CustomersDataView(ListView):
    #Customers Data View

    template_name = 'data.html'
    model = Customer
    paginate_by = 20
    context_object_name = 'costumers'

class UserViewSet(viewsets.ModelViewSet):
    #API endpoint

    queryset = Customer.objects.all()
    serializer_class = UserSerializer