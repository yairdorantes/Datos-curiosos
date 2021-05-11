
from django.contrib import admin
from django.urls import path
from .views import show_data,view_dato
urlpatterns = [
    path('curiosos/',show_data,name='show_datos'), 
    path('update/',view_dato,name='update_datos'),  
]

