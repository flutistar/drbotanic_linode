from django.shortcuts import render
from .models import Customer, Trip, Contact, Faq, Favicon


def home(request):
    trip = Trip.objects.all()
    customers = Customer.objects.all()
    favicon = Favicon.objects.all()[:1].get()
    context = {
        'customers': customers,
        'trip':trip[0].trip_link, 
        'title': 'DrBotanic Nutrition',
        'favicon': favicon
        }
    return render(request, 'home.html', context)


def contact(request):
    contact = Contact.objects.all()
    faqs = Faq.objects.all()
    context = {
        'faqs': faqs,
        'contact': contact[0].content, 
        'title': 'Contact Us'
    }
    return render(request, 'contact.html', context)
def faq(request):
    faqs = Faq.objects.all()
    context = {
        'faqs': faqs, 
        'title': 'FAQ'}
    return render(request, 'faq.html', context)