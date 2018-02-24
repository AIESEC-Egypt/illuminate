from django.shortcuts import render
from .models import Complaint
from .forms import ComplaintForm

def home(request):
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
    return render(request, "complaint.html", context)
