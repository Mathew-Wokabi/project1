from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt

from registration.models import student



from django.shortcuts import render
from django.http import JsonResponse
from .models import product
from .serializers import productSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def product_list(request , format=None):
  if request.method == 'GET':
    products = product.objects.all()
    serializer = productSerializer(products, many=True)
    return Response(serializer.data)

from django.shortcuts import render
from django.http import JsonResponse
from .models import product
from .serializers import carsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def cars_list(request , format=None):
  if request.method == 'GET':
    cars = product.objects.all()
    serializer = carsSerializer(cars, many=True)
    return Response(serializer.data)






def registration(request):
  template = loader.get_template('register.html')
  return HttpResponse(template.render())

def mypage(request):
  template = loader.get_template('register.html')
  return HttpResponse(template.render())

def home(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())

def courses(request):
  template = loader.get_template('courses.html')
  return HttpResponse(template.render())

def login(request):
  #template = loader.get_template('login.html')
  #return HttpResponse(template.render())
  return render(request, 'login.html')

def dashboard(request):
  data=student.objects.all()
  return render(request, 'dashboard.html',context={'data':data})



@csrf_exempt
def addstudent(request):
  if request.method == 'POST':
    formname = request.POST.get('studname')
    formemail = request.POST.get('studmail')
    formage = request.POST.get('studage')

    obj1=student(studentname=formname,email=formemail,age=formage)
    obj1.save()
  # fetch the student data to be displayed
  mydata =student.objects.all()
  context = {'data': mydata}
  return render(request, 'dashboard.html', context)


def editstudent(request,id):
    data = student.objects.get(id=id);
    context = {'data': data}
    return render(request, 'updatestudent.html', context)

def updatestudent(request,id):
  if request.method == 'POST':
    name = request.POST.get('studname')
    email = request.POST.get('studmail')
    age = request.POST.get('studage')

    #modify the student details based on the student id given
    editstudent = student.objects.get(id=id)#here  fetch the student to be changed

    #i make changes based on what came from the database
    editstudent.studentname=name
    editstudent.email=email
    editstudent.age=age
    #here i am saving the changes
    editstudent.save()
    return redirect('/dashboard')


def deletestudent(request,id):
  deletestudent = student.objects.get(id=id)
  deletestudent.delete()
  return redirect('/dashboard')




















