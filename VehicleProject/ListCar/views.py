from django.shortcuts import render,redirect
from .forms import CarModelForm
from .models import Car
from django.core.paginator import Paginator
from Home.models import Enquiry

def addCar(request):
    form = CarModelForm()
    if request.method == 'POST':
        form = CarModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('submit_car')
    template_name = 'dashboardapp/addcar.html'
    context = {'form':form}
    return render(request,template_name,context)

def submit(request):
    return render(request,'dashboardapp/submit.html')


def showCar(request):
    listcar = Car.objects.all()
    if request.method == 'POST':
        listcar = Car.objects.filter(year__icontains=request.POST['searchdata'])
        template_name = 'dashboardapp/searchcar.html'
        context = {'listcar':listcar}
        return render(request,template_name,context)
    paginator = Paginator(listcar,10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    template_name = 'dashboardapp/showcar.html'
    context = {'page_obj':page_obj}
    return render(request,template_name,context)

def buy_car(request,i):
    page_obj = Car.objects.get(id=i)
    page_obj.is_buy = True
    page_obj.save()
    return redirect('show_car')

def deleteCar(request,i):
    page_obj = Car.objects.get(id=i)
    page_obj.delete()
    return redirect('show_car')

'''
def addCar(request,i):
    obj_page = Car.objects.get(id=i)
    form = RCarModelForm(initial={'obj_page':obj_page})
    if request.user.status == 'mike@example.org':
        form = CarModelForm()
    if request.method == 'POST':
        form = RCarModelForm(request.POST)
        if request.user.status == 'mike@example.org':
            form = CarModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('submit_car')
    template_name = 'dashboardapp/addcar.html'
    context = {'form':form}
    return render(request,template_name,context)
'''