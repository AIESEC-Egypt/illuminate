from django.shortcuts import render
from .models import Ticket, Ep, Filler
from .forms import ComplaintEPForm, RequestEPForm


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
    }

    return render(request, 'forms/create_request.html', context)



# from .models import Request
# from .forms import RequestForm
#
# def create_request(request):
#     title = "Kindly Insert Your Request"
#     form = RequestForm(request.POST or None)
#     context = {
#         "title": title,
#         "requestform": form,
#     }
#     if request.user.is_authenticated() and request.user.is_staff:
#         queryset = Request.objects.all().order_by('-timestamp')
#         context = {
#             "queryset": queryset
#         }
#     return render(request, "forms/create_request.html", context)


# def create_complaint(request):
#     title = "Kindly Insert Your Complaint"
#     form = ComplaintForm(request.POST or None)
#     context = {
#         "title": title,
#         "complaintform": form,
#     }
#     if request.user.is_authenticated() and request.user.is_staff:
#         queryset = Complaint.objects.all().order_by('-timestamp')
#         context = {
#             "queryset": queryset
#         }
#     return render(request, "forms/create_complaint.html", context)
#
#
# def complaints_list(request):
#
#     title = 'Complaints List'
#
#     complaints = Complaint.objects.all()
#
#     context = {
#         "title": title,
#         "forms": complaints,
#     }
#
#     return render(request,"forms/complaints_list.html",context)
