from django.shortcuts import render
from .forms import get_general_statistics, get_time_analysis, get_location_analysis, get_worker_efficiency

def analytics_view(request):
    general_stats = get_general_statistics()
    time_analysis = get_time_analysis()
    location_analysis = get_location_analysis()
    worker_efficiency = get_worker_efficiency()

    return render(request, 'analytics/dashboard.html', {
        'general_stats': general_stats,
        'time_analysis': time_analysis,
        'location_analysis': location_analysis,
        'worker_efficiency': worker_efficiency,
    })
