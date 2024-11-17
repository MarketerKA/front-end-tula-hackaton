from django.urls import path
from .views import general_statistics_view, time_analysis_view, location_analysis_view, worker_efficiency_view

urlpatterns = [
    path('general/', general_statistics_view, name='general-statistics'),
    path('time/', time_analysis_view, name='time-analysis'),
    path('location/', location_analysis_view, name='location-analysis'),
    path('worker/', worker_efficiency_view, name='worker-efficiency'),
]
