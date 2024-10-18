from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name='home'),
    path('indic-philosophy/', views.indic_philosophy, name='indic_philosophy'),
    
]