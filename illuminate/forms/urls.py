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
]

