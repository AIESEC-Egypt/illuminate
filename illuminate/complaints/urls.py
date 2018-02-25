from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.create_complaint,
        name='create_complaint'
    ),

    url(
        regex=r'^view/$',
        view=views.complaints_list,
        name='view_complaints'
    ),
]
