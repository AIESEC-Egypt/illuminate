from importlib import import_module
from django import forms

from .models import *


class InitialProcessForm(forms.ModelForm):
    class Meta:
        model = Process
        fields = ['process_type', 'process_state']
        widgets = {'process_type': forms.HiddenInput(),
                   'process_state': forms.HiddenInput()}


#Complaint Related Forms
class ComplaintForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ComplaintForm, self).__init__(*args, **kwargs)
        self.fields['program'].required = True
        self.fields['complaint'].required = True
        self.fields['complaint_tag'].required = True


    class Meta:
        model = Ticket
        fields = ['program', 'complaint', 'complaint_tag']
class CoEPForm(forms.ModelForm):
    class Meta:
        model = Ep
        fields = ['ep_name', 'ep_country', 'ep_host_lc', 'ep_number', 'ep_email']

class ComplaintUpdateForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['ecb_responsible', 'standards']
class ComplaintProcessForm(forms.ModelForm):
    class Meta:
        model = Process
        fields = ('set_ecb_responsible', 'choose_standards', 'contacted_host', 'host_contact_output', 'contacted_ep',
                  'ep_contact_output', 'complaint_state', 'reason', 'process_state')


#Request Related Forms
class RequestForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RequestForm, self).__init__(*args, **kwargs)
        self.fields['program'].required = True
        self.fields['requested_break'].required = True
        self.fields['request_Reason'].required = True


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

#Case Related Forms
class CaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CaseForm, self).__init__(*args, **kwargs)
        self.fields['program'].required = True
        self.fields['case_mail_subject'].required = True
        self.fields['case_brief'].required = True
        self.fields['standards'].required = True


    standards = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(), queryset=Standard.objects.all())
    class Meta:
        model = Ticket
        fields = ['program', 'case_mail_subject', 'case_brief', 'standards']
class CaEPForm(forms.ModelForm):
    class Meta:
        model = Ep
        fields = ['ep_name', 'ep_country', 'ep_host_lc', 'ep_lc', 'ep_expa_id', 'opp_id']


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
    form_classes = [CoEPForm, ComplaintForm, InitialProcessForm]
class RequestEPForm(CombinedFormBase):
    form_classes = [ReFillerForm, ReEPForm, RequestForm, InitialProcessForm]
class CaseEPForm(CombinedFormBase):
    form_classes = [CaseForm, CaEPForm, InitialProcessForm]

# class ComplaintProcessUpdateForm(CombinedFormBase):
#     form_classes = [ComplaintUpdateForm, ComplaintProcessForm]


