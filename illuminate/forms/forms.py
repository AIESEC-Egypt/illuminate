from django import forms
from .models import Complaint,Request

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['full_name', 'whatsapp_number', 'email', 'country', 'program', 'host_lc', 'complaint','complaint_tag']

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['full_name', 'lc', 'position', 'role',
                  'ep_name', 'ep_entity', 'ep_email','ep_lc','ep_id','opp_id',
                  'requested_break','program','request_Reason'
                  ]
