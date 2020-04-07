from django.contrib import admin
from .models import Contact, Customer, Trip, Faq, Favicon

@admin.register(Contact, Customer, Trip, Faq, Favicon)
class CustomerAdmin(admin.ModelAdmin):
    pass