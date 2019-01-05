#Customer Data urls

#Django
from django.urls import path

#Local
from . import views

urlpatterns =[
    path('',views.index, name='index'),
    path('data/',views.CustomersDataView.as_view() ,name='data'),
]