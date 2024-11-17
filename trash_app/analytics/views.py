from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Bid
from django.db.models import Count, Avg, F, DurationField, ExpressionWrapper

@api_view(['GET'])
def general_statistics_view(request):
    total_bids = Bid.objects.count()
    resolved_bids = Bid.objects.filter(status='completed').count()
    active_bids = Bid.objects.exclude(status='completed').count()
    resolution_rate = (resolved_bids / total_bids * 100) if total_bids else 0

    data = {
        'total_bids': total_bids,
        'resolved_bids': resolved_bids,
        'active_bids': active_bids,
        'resolution_rate': resolution_rate,
    }
    return Response(data)

@api_view(['GET'])
def time_analysis_view(request):
    avg_reaction_time = Bid.objects.annotate(
        reaction_time=ExpressionWrapper(
            F('assigned_worker__user__date_joined') - F('created_at'),
            output_field=DurationField()
        )
    ).aggregate(Avg('reaction_time'))['reaction_time__avg']

    avg_completion_time = Bid.objects.annotate(
        completion_time=ExpressionWrapper(
            F('updated_at') - F('created_at'),
            output_field=DurationField()
        )
    ).aggregate(Avg('completion_time'))['completion_time__avg']

    data = {
        'avg_reaction_time': avg_reaction_time,
        'avg_completion_time': avg_completion_time,
    }
    return Response(data)

@api_view(['GET'])
def location_analysis_view(request):
    hotspots = Bid.objects.values('address').annotate(total=Count('id')).order_by('-total')[:10]
    return Response(hotspots)

@api_view(['GET'])
def worker_efficiency_view(request):
    efficiency = Bid.objects.values('assigned_worker__user__username').annotate(
        processed=Count('id'),
        avg_completion_time=Avg(
            ExpressionWrapper(
                F('updated_at') - F('created_at'),
                output_field=DurationField()
            )
        )
    ).order_by('-processed')
    return Response(efficiency)
