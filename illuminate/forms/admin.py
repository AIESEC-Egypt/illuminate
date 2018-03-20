from django.contrib import admin

from .models import Ticket, Ep, Filler
from .forms import ComplaintForm, EpComplaintForm

class ComplaintAdmin(admin.ModelAdmin):
    list_display = ['program', 'complaint', 'complaint_tag']
    form = ComplaintForm
    class Meta:
        model = Ticket

admin.site.register(Ticket)

# class RequestAdmin(admin.ModelAdmin):
#     list_display = ['full_name', 'lc', 'position', 'role',
#                   'ep_name', 'ep_entity', 'ep_email','ep_lc','ep_id','opp_id',
#                   'requested_break','program','request_Reason',
#                   "timestamp","updated"]
#     form = RequestForm
#     class Meta:
#         model = Request
#
#
# admin.site.register(Request)

