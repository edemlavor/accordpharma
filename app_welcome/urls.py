from django.urls import path
from . import views

urlpatterns = [
    
    # AFFICHAGE
    path('', views.PageWelcome, name='welcome'),

]