from django.contrib import admin

from .models import Request
from .forms import RequestForm

class RequestAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'lc', 'position', 'role',
                  'ep_name', 'ep_entity', 'ep_email','ep_lc','ep_id','opp_id',
                  'requested_break','program','request_Reason',
                  "timestamp","updated"]
    form = RequestForm
    class Meta:
        model = Request


admin.site.register(Request)
