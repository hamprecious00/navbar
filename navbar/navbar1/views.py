from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    # Add your Home tab logic here
    return render(request,'home.html',{})

def about_us(request):
    # Add your About Us tab logic here
    return render(request, 'about_us.html',{})

def contact(request):
    # Add your Contact tab logic here
    return render(request, 'contact.html')

def team_members(request):
    # Add your Team Members tab logic here
    return render(request, 'team_members.html')
