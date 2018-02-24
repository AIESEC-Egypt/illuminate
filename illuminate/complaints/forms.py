from django import forms
from .models import Complaint

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['full_name', 'whatsapp_number', 'email', 'country', 'program', 'host_lc', 'complaint','complaint_tag']
