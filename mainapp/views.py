from django.shortcuts import render
from .models import htmlfields
from random import choice
# Create your views here.

def home(request):
    fields = htmlfields.objects.all()

    return render(request,'index.html',{'data':fields[len(fields)-1]})

def stuff(request):
    fields = htmlfields.objects.all()
    mydata = choice(fields)
    return render(request,'index.html',{'data':mydata})


def live(request):
    return render(request,'live.html')

def about(request):
    return render(request,'aboutus.html')

def category(request):
    fields = htmlfields.objects.all()
    categories = []
    for field in fields:
        if field.category not in categories:
            categories.append(field.category)
    fields = htmlfields.objects.filter(category=choice(categories))
    if len(fields):
        message = False
    else:
        message = True
    return render(request,'category.html',{"query":fields,"ans":categories,"message":message})

def query(request):
    fields = htmlfields.objects.all()
    categories = []
    for field in fields:
        if field.category not in categories:
            categories.append(field.category)
    fields = {}        
    if request.method=='POST':
        data = request.POST['data']
        filters = request.POST['filters']
        if filters.lower() == 'author':
            fields = htmlfields.objects.filter(name=data)
        elif filters.lower() == 'title':
            fields = htmlfields.objects.filter(title=data)
        elif filters.lower() == 'location':
            fields = htmlfields.objects.filter(place=data)
        elif filters.lower() == 'category':
            fields = htmlfields.objects.filter(category=data)
        else:
            fields = htmlfields.objects.filter(timestamp=data)
    if len(fields):
        message = False
    else:
        message = True
    return render(request,'category.html',{"query":fields,"ans":categories,"message":message})

def mychoice(request):
    if request.method == 'POST':
        fields = htmlfields.objects.get(title=request.POST['queryme'])
        return render(request,'index.html',{'data':fields})