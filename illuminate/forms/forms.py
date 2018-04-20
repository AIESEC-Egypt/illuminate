from django import forms

from .models import *


#Complaint Related Forms
class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['program', 'complaint', 'complaint_tag']


class CoEPForm(forms.ModelForm):
    class Meta:
        model = Ep
        fields = ['ep_name', 'ep_country', 'ep_host_lc', 'ep_number', 'ep_email']


#Request Related Forms
class RequestForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['program', 'requested_break', 'request_Reason']


class ReEPForm(forms.ModelForm):
    class Meta:
        model = Ep
        fields = ['ep_name', 'ep_country', 'ep_number', 'ep_email', 'ep_expa_id', 'opp_id']


class ReFillerForm(forms.ModelForm):
    class Meta:
        model = Filler
        fields = ['filler_name', 'filler_email', 'filler_lc', 'filler_position', 'filler_role']


#Form Combining Class
class CombinedFormBase(forms.Form):
    form_classes = []

    def __init__(self, *args, **kwargs):
        super(CombinedFormBase, self).__init__(*args, **kwargs)
        for f in self.form_classes:
            name = f.__name__.lower()
            setattr(self, name, f(*args, **kwargs))
            form = getattr(self, name)
            self.fields.update(form.fields)
            self.initial.update(form.initial)

    def is_valid(self):
        isValid = True
        for f in self.form_classes:
            name = f.__name__.lower()
            form = getattr(self, name)
            if not form.is_valid():
                isValid = False
        # is_valid will trigger clean method
        # so it should be called after all other forms is_valid are called
        # otherwise clean_data will be empty
        if not super(CombinedFormBase, self).is_valid():
            isValid = False
        for f in self.form_classes:
            name = f.__name__.lower()
            form = getattr(self, name)
            self.errors.update(form.errors)
        return isValid

    def clean(self):
        cleaned_data = super(CombinedFormBase, self).clean()
        for f in self.form_classes:
            name = f.__name__.lower()
            form = getattr(self, name)
            cleaned_data.update(form.cleaned_data)
        return cleaned_data


#combined Forms
class ComplaintEPForm(CombinedFormBase):
    form_classes = [CoEPForm, ComplaintForm]


class RequestEPForm(CombinedFormBase):
    form_classes = [ReFillerForm, ReEPForm, RequestForm]
