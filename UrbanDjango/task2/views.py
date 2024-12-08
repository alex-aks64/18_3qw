from django.shortcuts import render
from django.views.generic import TemplateView


class index2(TemplateView):
    template_name = 'index2.html'
def index(request):
    return render(request,'index.html')

# Create your views here.
