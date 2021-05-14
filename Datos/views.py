from django.shortcuts import render,redirect
from .forms import formupost
from .models import Dato
import random
from django.db.models import Q
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

def sorted(request):
    lista = []
    datos_order = Dato.objects.all()
    for i in datos_order:
        lista.append(i)
    random.shuffle(lista)
    queryset = request.GET.get('buscar')
    
    if queryset:
        lista = Dato.objects.filter(
            Q(id__icontains = queryset) | 
            Q(autor = queryset)
        )

    return render(request, 'Datos/index.html',{'shuffle_data':lista})
def sorted_two(request):
    lista = []
    datos_order = Dato.objects.all()
    for i in datos_order:
        lista.append(i)
    random.shuffle(lista)
    queryset = request.GET.get('buscar')
    
    if queryset:
        lista = Dato.objects.filter(
            Q(id__icontains = queryset) | 
            Q(autor = queryset)
        )

    return render(request, 'Datos/two.html',{'shuffle_data':lista})