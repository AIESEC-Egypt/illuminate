from django import forms
from .models import *

class ComplaintForm(forms.ModelForm):
    ep_name = forms.CharField(max_length=128, help_text="Enter Your Full Name.")
    ep_number = forms.IntegerField(min_value=-9223372036854775808, max_value= 9223372036854775807, help_text="Enter the number with country code.")
    ep_email = forms.EmailField()
    # ep_host_lc = forms.ModelChoiceField(queryset=Offices)

    # 'ep_name', 'ep_number', 'ep_email', 'host_lc', 'ep_country',

    class Meta:
        model = Ticket
        fields = ['program', 'complaint', 'complaint_tag']


# class ComplaintForm(forms.ModelForm):
#     class Meta:
#         model = Complaint
#         fields = ['full_name', 'whatsapp_number', 'email', 'country', 'program', 'host_lc', 'complaint','complaint_tag']
#
# class RequestForm(forms.ModelForm):
#     class Meta:
#         model = Request
#         fields = ['responsible_name', 'responsible_lc', 'responsible_position', 'responsible_role',
#                   'ep_name', 'ep_entity', 'ep_email','ep_id','opp_id',
#                   'requested_break','program','request_Reason'
#                   ]
