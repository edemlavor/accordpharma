from django.urls import path
from . import views

urlpatterns = [
    
    # AFFICHAGE
    #path('', views.PageRepresentation, name='about'),
    path('consommable/', views.PageConsommable, name='consommable'),
    path('promotion/', views.PagePromotion, name='promotion'),
    path('import_export/', views.PageImport_Export, name='import_export'),
    path('complement/', views.PageComplement, name='complement'),
    path('representation/', views.PageRepresentation, name='representation'),
    path('catalogue/', views.PageCatalogue, name='catalogue'),
    
]