from django import forms
from .models import Request
from .models import Ticket, Ep, Filler

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['program', 'complaint', 'complaint_tag']

class EpComplaintForm(forms.ModelForm):
    class Meta:
        model = Ep
        fields = ['ep_name', 'ep_number', 'ep_email', 'host_lc', 'ep_country']




# class ComplaintForm(forms.ModelForm):
#     class Meta:
#         model = Complaint
#         fields = ['full_name', 'whatsapp_number', 'email', 'country', 'program', 'host_lc', 'complaint','complaint_tag']
#
class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['responsible_name', 'responsible_lc', 'responsible_position', 'responsible_role',
                  'ep_name', 'ep_entity', 'ep_email','ep_id','opp_id',
                  'requested_break','program','request_Reason'
                  ]
