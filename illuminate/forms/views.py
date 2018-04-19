from django.shortcuts import render

from illuminate.forms.models import Ticket, Ep
from .forms import ComplaintEPForm


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

            EP = Ep()
            EP.ep_name = form.cleaned_data['ep_name']
            EP.ep_number = form.cleaned_data['ep_number']
            EP.ep_email = form.cleaned_data['ep_email']
            EP.save()
            ticket.ep = EP
            ticket.save()
    else:
        form = ComplaintEPForm()

    context = {
        "title": title,
        "form": form,
    }

    return render(request, 'forms/create_complaint.html', context)


def form_valid(self, form):
    """
    If the form is valid, respond with success
    """
    first_name = form.cleaned_data.pop('first_name')
    last_name = form.cleaned_data.pop('last_name')
    email = form.cleaned_data.pop('email')

    user = User(
        first_name=first_name,
        last_name=last_name,
        email=email,
        username=email)
    user.save()

    user.set_password(form.cleaned_data.pop('password'))
    user.save()

    form.cleaned_data.update({'user': user})

    profile = Profile(**form.cleaned_data)
    profile.save()

    success_url = 'Registeration Successful, your data will be reviewed and you will be emailed once your data is approved'
    messages.success(self.request, success_url)
    return JsonResponse(
        {'details': success_url, 'success_url': reverse('login')})

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
