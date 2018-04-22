from django.contrib import admin

from .forms import ComplaintForm
from .models import *


class TicketAdmin(admin.ModelAdmin):
    list_display = ('ticket_type', 'program', 'timestamp')
    form = ComplaintForm



admin.site.register(Ticket)
admin.site.register(Position)
admin.site.register(Office)
admin.site.register(Role)
admin.site.register(Ep)
admin.site.register(Filler)
admin.site.register(Standard)



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
