from django.shortcuts import render
from .models import Ticket, Ep, Filler
from .forms import ComplaintForm, EpComplaintForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response


def create_complaint(request):
    if request.method == "POST":
        complaintform = ComplaintForm(request.POST, instance=Ticket())
        epcomplaintform = EpComplaintForm(request.POST, instance=Ep())

        if complaintform.is_valid() and epcomplaintform.is_valid():  # All validation rules pass
            new_complaint = complaintform.save()
            new_ep = epcomplaintform.save()
            new_ep.complaint = new_complaint
            new_ep.save()
            return HttpResponseRedirect("/")

    else:
        title = "Kindly Insert Your Complaint"
        complaintform = ComplaintForm(instance=Ticket())
        epcomplaintform = EpComplaintForm(instance=Ep())
        context = {
                "title": title,
                "complaintform": complaintform,
                "epcomplaintform": epcomplaintform,
            }
        return render(request, 'forms/create_complaint.html', context)



from .models import Request
from .forms import RequestForm


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
def create_request(request):
    title = "Kindly Insert Your Request"
    form = RequestForm(request.POST or None)
    context = {
        "title": title,
        "requestform": form,
    }
    if request.user.is_authenticated() and request.user.is_staff:
        queryset = Request.objects.all().order_by('-timestamp')
        context = {
            "queryset": queryset
        }
    return render(request, "forms/create_request.html", context)

