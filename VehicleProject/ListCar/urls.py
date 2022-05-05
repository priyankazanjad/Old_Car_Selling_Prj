from django.urls import path
from . import views

urlpatterns = [
    path('add/',views.addCar,name='add_car'),
    path('show/',views.showCar,name='show_car'),
    path('appr/<int:i>/',views.buy_car,name='approve'),
    path('sub/',views.submit,name='submit_car'),
    path('del/<int:i>/',views.deleteCar,name='delete')
]
