from django.shortcuts import render
from django.contrib import messages

# Create your views here.

def message(request):
    return render(request,'message.html')

def success(request):
    messages.success(request,'This is success message')
    return render(request,'message.html')

def info(request):
    messages.success(request,'This is info message')
    return render(request,'message.html')

def error(request):
    messages.error(request,'This is error message')
    return render(request,'message.html')

def warning(request):
    messages.warning(request,'This is warning message')
    return render(request,'message.html')