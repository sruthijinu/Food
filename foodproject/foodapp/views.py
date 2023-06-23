from django.http import HttpResponse
from django.shortcuts import render, redirect
from .form import FoodForm
from .models import Food
# Create your views here.
def index(request):
    obj=Food.objects.all()
    return render(request,'index.html',{'key1':obj})
def detail(request,food_id):
    obj1=Food.objects.get(id=food_id)
    return render(request,'detail.html',{'key2':obj1})
def add_food(request):
    if request.method=="POST":
        name=request.POST.get('name', )
        desc=request.POST.get('desc', )
        price=request.POST.get('price', )
        img=request.FILES['img']
        food=Food(name=name,desc=desc,price=price,img=img)
        food.save()
    return render(request,'add_food.html')
def update(request,id):
    food_update=Food.objects.get(id=id)
    food_form=FoodForm(request.POST or None, request.FILES,instance=food_update)
    if food_form.is_valid():
         food_form.save()
         return redirect('/')
    return render(request,'update.html',{'key3':food_form,'key4':food_update})
def delete(request,id):
    if request.method=="POST":
        food_del=Food.objects.get(id=id)
        food_del.delete()
        return redirect('/')
    return render(request,'delete.html')


