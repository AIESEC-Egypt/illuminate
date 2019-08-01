from django.shortcuts import render, redirect
import django.db.models
from illuminate.forms.models import *

def user_anlaytics(request):

    # initiation data
    offices = Office.objects.order_by('office_name')
    current_user = request.user
    current_user_manager = request.user.manager
    total_tickets = Ticket.objects.all()
    team_tickets = total_tickets.filter(ecb_responsible__manager__name=current_user_manager)
    user_tickets = total_tickets.filter(ecb_responsible=current_user)

    # total absolute numbers
    total_tickets_count = total_tickets.count()
    total_complaints_count = total_tickets.filter(ticket_type='Complaint').count()
    total_requests_count = total_tickets.filter(ticket_type='Request').count()
    total_cases_count = total_tickets.filter(ticket_type='Case').count()


    # Team absolute numbers
    team_tickets_count = team_tickets.count()
    team_complaints_count = team_tickets.filter(ticket_type='Complaint').count()
    team_requests_count = team_tickets.filter(ticket_type='Request').count()
    team_cases_count = team_tickets.filter(ticket_type='Case').count()


    # user absolute numbers
    user_tickets_count = user_tickets.count()
    user_complaints_count = user_tickets.filter(ticket_type='Complaint').count()
    user_complaints_count_open = user_tickets.filter(ticket_type='Complaint', ticket_state='Open').count()
    user_complaints_count_in_progress = user_tickets.filter(ticket_type='Complaint', ticket_state='In Progress').count()
    user_complaints_count_closed = user_tickets.filter(ticket_type='Complaint', ticket_state='Closed').count()

    user_requests_count = user_tickets.filter(ticket_type='Request').count()
    user_requests_count_open = user_tickets.filter(ticket_type='Request', ticket_state='Open').count()
    user_requests_count_in_progress = user_tickets.filter(ticket_type='Request', ticket_state='In Progress').count()
    user_requests_count_closed = user_tickets.filter(ticket_type='Request', ticket_state='Closed').count()

    user_cases_count = user_tickets.filter(ticket_type='Case').count()
    user_cases_count_open = user_tickets.filter(ticket_type='Case', ticket_state='Open').count()
    user_cases_count_in_progress = user_tickets.filter(ticket_type='Case', ticket_state='In Progress').count()
    user_cases_count_closed = user_tickets.filter(ticket_type='Case', ticket_state='Closed').count()

    # user relative numbers
    # total_Complaint_contribution = (user_complaints_count/total_complaints_count)*100


    context = {
        "offices": offices,
        "current_user": current_user,
        "current_user_manager": current_user_manager,
        "tickets": total_tickets,
        "user_tickets": user_tickets,

        # total absolute numbers
        "total_tickets_count": total_tickets_count,
        "total_complaints_count": total_complaints_count,
        "total_requests_count": total_requests_count,
        "total_cases_count": total_cases_count,

        # Team absolute numbers
        "team_tickets_count": team_tickets_count,
        "team_complaints_count": team_complaints_count,
        "team_requests_count": team_requests_count,
        "team_cases_count": team_cases_count,

        # user absolute numbers
        "user_tickets_count": user_tickets_count,

        "user_complaints_count": user_complaints_count,
        "user_complaints_count_open": user_complaints_count_open,
        "user_complaints_count_in_progress": user_complaints_count_in_progress,
        "user_complaints_count_closed": user_complaints_count_closed,

        "user_requests_count": user_requests_count,
        "user_requests_count_open": user_requests_count_open,
        "user_requests_count_in_progress": user_requests_count_in_progress,
        "user_requests_count_closed": user_requests_count_closed,

        "user_cases_count": user_cases_count,
        "user_cases_count_open": user_cases_count_open,
        "user_cases_count_in_progress": user_cases_count_in_progress,
        "user_cases_count_closed": user_cases_count_closed,

        # "total_Complaint_contribution": total_Complaint_contribution,

    }

    return render(request, 'analytics/user_analytics.html', context=context)


def lc_analytics(request, office_name):
    tickets = Ticket.objects.all()
    # complaints = Ticket.objects.filter(ticket_type='Complaint')
    # my_lc = Office.objects.get(pk=office_name)
    # lc = OfficeSnapshot.objects.get(office=my_lc)
    #
    offices = Office.objects.order_by('office_name')

    my_lc = Office.objects.get(pk=office_name)

    lc = Office.objects.get(office_name=my_lc)
    lc_name = my_lc.office_name
    lc_complaints_count = Ticket.objects.filter(ticket_type='Complaint', office__office_name=office_name).count()

    context = {
        "offices": offices,
        "lc_complaints_count": lc_complaints_count,
        "lc_name": lc_name,
        "lc": lc,
        "my_lc": my_lc,
        # "office": office,
    }

    return render(request, "analytics/lc_analytics.html", context)


def home_view(request):

    if request.user.is_authenticated():

        offices = Office.objects.order_by('office_name')
        tickets = Ticket.objects.all()

        current_user = request.user

        user = Ticket.objects.filter(ecb_responsible=current_user)

        # complaints data
        user_complaints_count = tickets.filter(ticket_type='Complaint').count()
        user_complaints_count_open = tickets.filter(ticket_type='Complaint', ticket_state='Open').count()
        user_complaints_count_in_progress = tickets.filter(ticket_type='Complaint', ticket_state='In Progress').count()
        user_complaints_count_closed = tickets.filter(ticket_type='Complaint', ticket_state='Closed').count()

        # requests data
        user_requests_count = tickets.filter(ticket_type='Request').count()
        user_requests_count_open = tickets.filter(ticket_type='Request', ticket_state='Open').count()
        user_requests_count_in_progress = tickets.filter(ticket_type='Request', ticket_state='In Progress').count()
        user_requests_count_closed = tickets.filter(ticket_type='Request', ticket_state='Closed').count()

        # cases data
        user_cases_count = tickets.filter(ticket_type='Case').count()
        user_cases_count_open = tickets.filter(ticket_type='Case', ticket_state='Open').count()
        user_cases_count_in_progress = tickets.filter(ticket_type='Case', ticket_state='In Progress').count()
        user_cases_count_closed = tickets.filter(ticket_type='Case', ticket_state='Closed').count()

        context = {
            "offices": offices,
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

        return render(request, "pages/home.html", context)
    else:
        return redirect("accounts/login")
