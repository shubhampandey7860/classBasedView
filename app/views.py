from django.shortcuts import render
from app.models import *
# Create your views here.
from django.views.generic import *
from django.urls import reverse_lazy

class Home(TemplateView):
    template_name='app/home.html'


class SchoolList(ListView):
    model =School
    context_object_name ='schools'
    #template_name='app/school_list.html'
    #queryset=School.objects.filter(name='Jspiders')
    ordering=['name'] 
    
    
class SchoolDetail(DetailView):
    model = School
    context_object_name ='sc' 
    
   
class SchoolCreate(CreateView):
    model = School
    fields = '__all__'
    
class SchoolUpdate(UpdateView):
    model = School
    fields = '__all__'
    
class SchoolDelete(DeleteView):
    model = School
    context_object_name = 'sc'
    success_url = reverse_lazy('SchoolList')
    

    
    
           
        
