from django.urls import path
from . import views
from rest_framework.urlpatterns import  format_suffix_patterns

urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('registerpage/', views.mypage, name='myregisterpage'),
    path('', views.home, name='myhome'),
    path('login/', views.login, name='myloginpage'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('addstudent',views.addstudent, name='addingstudent'),
    path('editstudent/<id>',views.editstudent, name='editstudent'),
    path('updatestudent/<id>',views.updatestudent, name='updatestudent'),
    path('deletestudent/<id>',views.deletestudent), #the url comes with the id as a parameter
    path('product/', views.product_list),
    path('cars/', views.cars_list),

]

urlpatterns = format_suffix_patterns(urlpatterns)
