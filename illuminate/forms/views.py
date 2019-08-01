from django.shortcuts import render
from .models import Ticket, Ep, Filler, Office
from .forms import ComplaintEPForm, RequestEPForm, CaseEPForm, ComplaintUpdateForm, RequestUpdateForm, CaseUpdateForm
from django.views.generic import UpdateView
from django.shortcuts import render_to_response


def create_complaint(request):
    title = "Kindly Insert Your Complaint"
    offices = Office.objects.order_by('office_name')

    if request.method == 'POST':
        form = ComplaintEPForm(request.POST)
        if form.is_valid():
            ticket = Ticket()
            ticket.program = form.cleaned_data['program']
            ticket.complaint = form.cleaned_data['complaint']
            # ticket.standards = form.cleaned_data['standards']
            ticket.ticket_type = "Complaint"
            ticket.ticket_state = "Draft"
            ticket.office = form.cleaned_data['ep_host_lc']

            if form.cleaned_data['ep_country'] == "Egypt":
                ticket.complaint_type = "OGX"
            else:
                ticket.complaint_type = "ICX"
            ep = Ep()
            ep.ep_name = form.cleaned_data['ep_name']
            ep.ep_country = form.cleaned_data['ep_country']
            ep.ep_host_lc = form.cleaned_data['ep_host_lc']
            ep.ep_number = form.cleaned_data['ep_number']
            ep.ep_email = form.cleaned_data['ep_email']

            ep.save()
            ticket.ep = ep
            ticket.save()
    else:
        form = ComplaintEPForm()

    context = {
        "title": title,
        "offices": offices,

    }

    return render(request, 'forms/create_complaint.html', context)


def create_request(request):
    title = "Kindly Insert Your Request"
    offices = Office.objects.order_by('office_name')

    if request.method == 'POST':
        form = RequestEPForm(request.POST)
        if form.is_valid():
            ticket = Ticket()
            ticket.program = form.cleaned_data['program']
            ticket.requested_break = form.cleaned_data['requested_break']
            ticket.request_Reason = form.cleaned_data['request_Reason']
            ticket.ticket_type = "Request"
            ticket.ticket_state = "Draft"
            ticket.office = form.cleaned_data['filler_lc']

            ep = Ep()
            ep.ep_name = form.cleaned_data['ep_name']
            ep.ep_country = form.cleaned_data['ep_country']
            ep.ep_number = form.cleaned_data['ep_number']
            ep.ep_email = form.cleaned_data['ep_email']
            ep.ep_expa_id = form.cleaned_data['ep_expa_id']
            ep.opp_id = form.cleaned_data['opp_id']
            ep.ep_host_lc = form.cleaned_data['filler_lc']

            filler = Filler()
            filler.filler_name = form.cleaned_data['filler_name']
            filler.filler_email = form.cleaned_data['filler_email']
            filler.filler_lc = form.cleaned_data['filler_lc']
            filler.filler_position = form.cleaned_data['filler_position']
            filler.filler_role = form.cleaned_data['filler_role']

            filler.save()
            ep.save()
            ticket.filler = filler
            ticket.ep = ep
            ticket.save()
    else:
        form = RequestEPForm()
    context = {
        "title": title,
        "form": form,
        "offices": offices,

    }

    return render(request, 'forms/create_request.html', context)


def create_case(request):
    title = "Kindly fill Case Information"
    offices = Office.objects.order_by('office_name')

    if request.method == 'POST':
        form = CaseEPForm(request.POST)
        if form.is_valid():
            ticket = Ticket()
            ticket.program = form.cleaned_data['program']
            ticket.case_mail_subject = form.cleaned_data['case_mail_subject']
            ticket.case_brief = form.cleaned_data['case_brief']
            ticket.standards = form.cleaned_data['standards']
            ticket.ticket_type = "Case"
            ticket.ticket_state = "Draft"
            ticket.office = form.cleaned_data['ep_host_lc']

            ep = Ep()
            ep.ep_name = form.cleaned_data['ep_name']
            ep.ep_number = form.cleaned_data['ep_number']
            ep.ep_country = form.cleaned_data['ep_country']
            ep.ep_lc = form.cleaned_data['ep_lc']
            ep.ep_email = form.cleaned_data['ep_expa_id']
            ep.ep_email = form.cleaned_data['opp_id']
            ep.ep_host_lc = form.cleaned_data['ep_host_lc']

            ep.save()
            ticket.ep = ep
            ticket.save()
    else:
        form = CaseEPForm()

    context = {
        "title": title,
        "form": form,
        "offices": offices,

    }

    return render(request, 'forms/create_case.html', context)


def tickets_list(request):
    offices = Office.objects.order_by('office_name')

    title = 'tickets List'
    tickets = Ticket.objects.all()

    current_user = request.user
    user = Ticket.objects.filter(ecb_responsible=current_user)

    # complaints data
    user_complaints_count = user.filter(ticket_type='Complaint').count()
    user_complaints_count_open = user.filter(ticket_type='Complaint', ticket_state='Open').count()
    user_complaints_count_in_progress = user.filter(ticket_type='Complaint', ticket_state='In Progress').count()
    user_complaints_count_closed = user.filter(ticket_type='Complaint', ticket_state='Closed').count()

    # requests data
    user_requests_count = user.filter(ticket_type='Request').count()
    user_requests_count_open = user.filter(ticket_type='Request', ticket_state='Open').count()
    user_requests_count_in_progress = user.filter(ticket_type='Request', ticket_state='In Progress').count()
    user_requests_count_closed = user.filter(ticket_type='Request', ticket_state='Closed').count()

    # cases data
    user_cases_count = user.filter(ticket_type='Case').count()
    user_cases_count_open = user.filter(ticket_type='Case', ticket_state='Open').count()
    user_cases_count_in_progress = user.filter(ticket_type='Case', ticket_state='In Progress').count()
    user_cases_count_closed = user.filter(ticket_type='Case', ticket_state='Closed').count()

    context = {
        "offices": offices,

        "title": title,
        "tickets": tickets,
        "user_complaints_count": user_complaints_count,
        "user_requests_count": user_requests_count,
        "user_cases_count": user_cases_count,

        "user_complaints_count_open": user_complaints_count_open,
        "user_complaints_count_in_progress": user_complaints_count_in_progress,
        "user_complaints_count_closed": user_complaints_count_closed,
        "user_requests_count_open": user_requests_count_open,
        "user_requests_count_in_progress": user_requests_count_in_progress,
        "user_requests_count_closed": user_requests_count_closed,
        "user_cases_count_open": user_cases_count_open,
        "user_cases_count_in_progress": user_cases_count_in_progress,
        "user_cases_count_closed": user_cases_count_closed,

    }

    return render(request, "forms/ticket_list.html", context)


class ComplaintUpdate(UpdateView):
    template_name = 'forms/edit_ticket.html'
    form_class = ComplaintUpdateForm
    model = Ticket

    # That should be all you need. If you need to do any more custom stuff
    # before saving the form, override the `form_valid` method, like this:

    def form_valid(self, form):
        self.object = form.save(commit=False)

        self.object.save()
        return render_to_response(self.template_name, self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super(ComplaintUpdate, self).get_context_data(**kwargs)
        context['offices'] = Office.objects.order_by('office_name')
        #whatever you would like

        return context


class RequestUpdate(UpdateView):
    template_name = 'forms/edit_ticket.html'
    form_class = RequestUpdateForm
    model = Ticket

    # That should be all you need. If you need to do any more custom stuff
    # before saving the form, override the `form_valid` method, like this:

    def form_valid(self, form):
        self.object = form.save(commit=False)

        self.object.save()
        return render_to_response(self.template_name, self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super(RequestUpdate, self).get_context_data(**kwargs)
        context['offices'] = Office.objects.order_by('office_name')
        #whatever you would like

        return context


class CaseUpdate(UpdateView):
    template_name = 'forms/edit_ticket.html'
    form_class = CaseUpdateForm
    model = Ticket

    # That should be all you need. If you need to do any more custom stuff
    # before saving the form, override the `form_valid` method, like this:

    def form_valid(self, form):
        self.object = form.save(commit=False)

        self.object.save()
        return render_to_response(self.template_name, self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super(CaseUpdate, self).get_context_data(**kwargs)
        context['offices'] = Office.objects.order_by('office_name')
        #whatever you would like

        return context
