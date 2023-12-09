from django.contrib import admin
from .models import contact,Newsletter

@admin.register(contact)
class contactAdmin(admin.ModelAdmin):
    date_hierarchy='created_date'
    list_display=('name','subject','email','created_date')
    list_filter=['subject']
    search_fields=['subject','message']
    class Meta:
        ordering=['-created_date']


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display=('email',)