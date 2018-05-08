from django.shortcuts import render
from .models import Ticket, Ep, Filler
from .forms import ComplaintEPForm, RequestEPForm, CaseEPForm


def create_complaint(request):
    title = "Kindly Insert Your Complaint"

    if request.method == 'POST':
        form = ComplaintEPForm(request.POST)
        if form.is_valid():
            ticket = Ticket()
            ticket.program = form.cleaned_data['program']
            ticket.complaint = form.cleaned_data['complaint']
            ticket.complaint_tag = form.cleaned_data['complaint_tag']
            ticket.ticket_type = "Complaint"
            ticket.ticket_state = "Open"
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
        "form": form,
    }

    return render(request, 'forms/create_complaint.html', context)


def create_request(request):
    title = "Kindly Insert Your Request"

    if request.method == 'POST':
        form = RequestEPForm(request.POST)
        if form.is_valid():
            ticket = Ticket()
            ticket.program = form.cleaned_data['program']
            ticket.requested_break = form.cleaned_data['requested_break']
            ticket.request_Reason = form.cleaned_data['request_Reason']
            ticket.ticket_type = "Request"
            ticket.ticket_state = "Open"

            ep = Ep()
            ep.ep_name = form.cleaned_data['ep_name']
            ep.ep_country = form.cleaned_data['ep_country']
            ep.ep_number = form.cleaned_data['ep_number']
            ep.ep_email = form.cleaned_data['ep_email']
            ep.ep_expa_id = form.cleaned_data['ep_expa_id']
            ep.opp_id = form.cleaned_data['opp_id']
            # ep.ep_host_lc = form.cleaned_data['filler_lc']

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
    }

    return render(request, 'forms/create_request.html', context)


def create_case(request):
    title = "Kindly fill Case Information"

    if request.method == 'POST':
        form = CaseEPForm(request.POST)
        if form.is_valid():
            ticket = Ticket()
            ticket.program = form.cleaned_data['program']
            ticket.case_mail_subject = form.cleaned_data['case_mail_subject']
            ticket.case_brief = form.cleaned_data['case_brief']
            ticket.standards = form.cleaned_data['standards']
            ticket.ticket_type = "Case"
            ticket.ticket_state = "Open"

            ep = Ep()
            ep.ep_name = form.cleaned_data['ep_name']
            ep.ep_country = form.cleaned_data['ep_country']
            ep.ep_host_lc = form.cleaned_data['ep_host_lc']
            ep.ep_number = form.cleaned_data['ep_lc']
            ep.ep_email = form.cleaned_data['ep_expa_id']
            ep.ep_email = form.cleaned_data['opp_id']

            ep.save()
            ticket.ep = ep
            ticket.save()
    else:
        form = CaseEPForm()

    context = {
        "title": title,
        "form": form,
    }

    return render(request, 'forms/create_case.html', context)


def tickets_list(request):

    title = 'tickets List'

    Tickets = Ticket.objects.all()

    context = {
        "title": title,
        "tickets": Tickets,
    }

    return render(request,"forms/ticket_list.html",context)

