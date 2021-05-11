from django.shortcuts import render
from .forms import formupost
from .models import Dato
# Create your views here.
def view_dato(request):
    form=formupost(request.POST, request.FILES)
    if request.method == 'POST':
        form = formupost(request.POST,request.FILES)
        if form.is_valid():
            datos = form.save(commit=False)
            dato = form.save()
    form = formupost()
    return render(request,'Datos/create_data.html',{'form':form})

def show_data(request):
    datos = Dato.objects.all()
    return render(request,'Datos/index.html',{'datos':datos})