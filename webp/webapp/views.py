from django.shortcuts import render
from .models import Place
from .models import Task
# Create your views here.
def index(request):
    obj=Place.objects.all()
    obj2=Task.objects.all()
    return render(request,"index.html",{'object' : obj , 'object2': obj2})
def about(request):
    return render(request,"about.html")
def blog(request):
    return render(request,"blog.html")
def contact(request):
    return render(request,"contact.html")
def detail(request):
    return render(request,"detail.html")
def project(request):
    return render(request,"project.html")
def service(request):
    return render(request,"service.html")
def team(request):
    return render(request,"team.html")
def testimonial(request):
    return render(request,"testimonial.html")

