from django.shortcuts import render
from .models import Complaint, Request
from .forms import ComplaintForm, RequestForm


def create_complaint(request):
    title = "Kindly Insert Your Complaint"
    form = ComplaintForm(request.POST or None)
    context = {
        "title": title,
        "complaintform": form,
    }
    if request.user.is_authenticated() and request.user.is_staff:
        queryset = Complaint.objects.all().order_by('-timestamp')
        context = {
            "queryset": queryset
        }
    return render(request, "forms/create_complaint.html", context)


def complaints_list(request):

    title = 'Complaints List'

    complaints = Complaint.objects.all()

    context = {
        "title": title,
        "forms": complaints,
    }

    return render(request,"forms/complaints_list.html",context)


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
