from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'master/home.html')

def approve(request):
    return render(request,'master/appro.html')