from django.contrib import admin
from .models import Contact, Customer, Trip, Faq

@admin.register(Contact, Customer, Trip, Faq)
class CustomerAdmin(admin.ModelAdmin):
    pass