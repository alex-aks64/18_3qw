
from django.shortcuts import render

def home(request):
    return render(request, 'second_task/index.html')

def shop(request):
    return render(request, 'second_task/index2.html')

def cart(request):
    return render(request, 'second_task/index3.html')
# Create your views here.

# Create your views here.
