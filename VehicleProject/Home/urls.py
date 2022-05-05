from django.urls import path
from . import views

urlpatterns = [
    path('enq/',views.enquiryview,name='enquiry'),
    path('eshow/',views.showenquiryview,name='showenq'),
    path('index/',views.index,name='sendmail'),
    path('home/',views.home,name='home'),

]