from django.urls import path
from .views import *

app_name = 'reports'

urlpatterns = [
    path('', home_view, name='home'),
    # path('accidents/', AccidentReportListCreateView.as_view(), name='accident-list-create'),
    path('accidents/', accident_list, name='accident_list'),
    path('accidents/<int:report_id>/upvote/', upvote_report, name='upvote_report'),
    path('report/', accident_report_view, name='report'),
    path('success/', success_view, name='success'),
]
