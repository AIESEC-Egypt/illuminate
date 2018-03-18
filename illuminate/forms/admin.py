from django.contrib import admin

from .models import Complaint, Request
from .forms import ComplaintForm, RequestForm

class ComplaintAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'whatsapp_number', 'email', 'country', 'program', 'host_lc', 'complaint','complaint_tag',"timestamp","updated"]
    form = ComplaintForm
    class Meta:
        model = Complaint


admin.site.register(Complaint)

class RequestAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'lc', 'position', 'role',
                  'ep_name', 'ep_entity', 'ep_email','ep_lc','ep_id','opp_id',
                  'requested_break','program','request_Reason',
                  "timestamp","updated"]
    form = RequestForm
    class Meta:
        model = Request


admin.site.register(Request)

