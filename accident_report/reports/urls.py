from django.urls import path
from .views import *

app_name = 'reports'

urlpatterns = [
    path('', home, name='home'),
    path('accidents/', accident_list, name='accident_list'),
    path('report/', accident_report_view, name='accident_report'),  # <-- rename here
    path('accidents/<int:report_id>/upvote/', upvote_report, name='upvote_report'),
    path('success/', success_view, name='success'),
    
]
