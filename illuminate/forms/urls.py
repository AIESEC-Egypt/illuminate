from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        regex=r'^complaint/$',
        view=views.create_complaint,
        name='create_complaint'
    ),
    url(
        regex=r'^request/$',
        view=views.create_request,
        name='create_request'
    ),
    url(
        regex=r'^case/$',
        view=views.create_case,
        name='create_case'
    ),
    url(
        regex=r'^ticket/$',
        view=views.tickets_list,
        name='ticket_list'
    ),
    url(
        regex=r'^edit/ticket/complaint/(?P<pk>[0-9]+)/$',
        view=views.ComplaintUpdate.as_view(),
        name='edit_complaint'
    ),
    url(
        regex=r'^edit/ticket/request/(?P<pk>[0-9]+)/$',
        view=views.RequestUpdate.as_view(),
        name='edit_request'
    ),
    url(
        regex=r'^edit/ticket/case/(?P<pk>[0-9]+)/$',
        view=views.CaseUpdate.as_view(),
        name='edit_case'
    ),
]

