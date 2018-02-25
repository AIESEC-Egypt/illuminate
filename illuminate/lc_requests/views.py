from django.shortcuts import render
from .models import Request
from .forms import RequestForm

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
    return render(request, "lc_requests/create_request.html", context)
