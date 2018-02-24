from django.contrib import admin

from .models import Complaint
from .forms import ComplaintForm

class ComplaintAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'whatsapp_number', 'email', 'country', 'program', 'host_lc', 'complaint','complaint_tag',"timestamp","updated"]
    form = ComplaintForm
    class Meta:
        model = Complaint


admin.site.register(Complaint)

