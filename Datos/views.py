from django.shortcuts import render,redirect
from .forms import formupost
from .models import Dato
# Create your views here.
def view_dato(request):
    if request.method == 'POST':
        form = formupost(request.POST,request.FILES)
        if form.is_valid():
            datosf = form.save(commit=False)
            datosf.save()
            return redirect('show_datos')
    form = formupost()
    return render(request,'Datos/create_data.html',{'form':form})

def show_data(request):
    datos = Dato.objects.all()
    return render(request,'Datos/index.html',{'datos':datos})