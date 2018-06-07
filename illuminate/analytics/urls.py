from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        regex=r'^user/$',
        view=views.user_anlaytics,
        name='user_analytics'
    ),
    url(
        regex=r'^lc/(?P<office_name>\w+)/$',
        view=views.lc_analytics,
        name='lc_analytics'
    ),

]

