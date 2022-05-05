from django.shortcuts import render,redirect
from .models import Enquiry
from .forms import EnquiryModelForm
from django.core.mail import send_mail
#from ListCar.models import Car
from django.core.mail import EmailMessage

def home(request):
    return render(request,'layout.html')

def enquiryview(request):
    form = EnquiryModelForm()
    if request.method == 'POST':
        form = EnquiryModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
    template_name = 'dashboardapp/enquiry.html'
    context = {'form':form}
    return render(request,template_name,context)

def showenquiryview(request):
    enquiry = Enquiry.objects.all()
    context = {'enquiry':enquiry}
    template_name = 'dashboardapp/showenquiry.html'
    return render(request,template_name,context)


def index(request):
    send_mail('Hello Mike',
    'Hello there,this is an automated message',
    'priyankazanjad95@gmail.com',
    ['priyankazanjad5@gmail.com'],
    fail_silently=False
              )
    return render(request,'dashboardapp/index.html')

'''
def enquiryview(request,i):
    form = EnquiryModelForm()
    if request.method == 'POST':
        form = EnquiryModelForm(request.POST)
        if form.is_valid():
            form.save()
            page_obj = Car.objects.get(id=i)
            page_obj.is_buy = True
            page_obj.save()
            name = request.data.get('name')
            mobile = request.data.get('mobile')
            print("SEnding mail")
            message = f'{page_obj.seller_name}'
            print(message)
            send_mail('Hello Mike',
                      message,
                      'priyankazanjad95@gmail.com',
                      ['priyankazanjad5@gmail.com'],
                      fail_silently=False
                      )
            print("mail_sent")
            return redirect('show_car')

    template_name = 'dashboardapp/enquiry.html'
    context = {'form':form}
    return render(request,template_name,context)
'''