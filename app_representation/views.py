from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect

# Create your views here.
def PageRepresentation(request):
    return render(request, 'representation/representation.html')

def PageConsommable(request):
    return render(request, 'representation/consommable.html')

def PagePromotion(request):
    return render(request, 'representation/promotion.html')

def PageImport_Export(request):
    return render(request, 'representation/import_export.html')

def PageComplement(request):
    return render(request, 'representation/complement.html')

def PageCatalogue(request):
    return render(request, 'representation/representation.html')