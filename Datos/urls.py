
from django.contrib import admin
from django.urls import path
from .views import view_dato,sorted,sorted_two
urlpatterns = [
    path('update/',view_dato,name='update_datos'),  
    path('random',sorted,name='sorted_data'),
    path('two/',sorted_two,name='sorted_two')
]

