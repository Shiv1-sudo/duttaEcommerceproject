from django.shortcuts import render
from duttaEcommerceapp.models.techservicesmodel import TechService

def tech_services(request):
    free_services = TechService.objects.filter(type='Free')
    paid_services = TechService.objects.filter(type='Paid')
    return render(request, 'tech_services.html', {'free_services': free_services, 'paid_services': paid_services})
