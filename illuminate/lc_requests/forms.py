from django import forms
from .models import Request

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['full_name', 'lc', 'position', 'role',
                  'ep_name', 'ep_entity', 'ep_email','ep_lc','ep_id','opp_id',
                  'requested_break','program','request_Reason'
                  ]
