from ..models import Bid
from django.db.models import Count, Avg, F, DurationField, ExpressionWrapper

# Общие показатели
def get_general_statistics():
    total_bids = Bid.objects.count()
    resolved_bids = Bid.objects.filter(status='completed').count()
    active_bids = Bid.objects.exclude(status='completed').count()
    resolution_rate = (resolved_bids / total_bids * 100) if total_bids else 0

    return {
        'total_bids': total_bids,
        'resolved_bids': resolved_bids,
        'active_bids': active_bids,
        'resolution_rate': resolution_rate,
    }

# Анализ по времени
def get_time_analysis():
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

    return {
        'avg_reaction_time': avg_reaction_time,
        'avg_completion_time': avg_completion_time,
    }

# Анализ по локациям
def get_location_analysis():
    hotspots = Bid.objects.values('address').annotate(total=Count('id')).order_by('-total')[:10]
    return hotspots

# Эффективность сотрудников
def get_worker_efficiency():
    efficiency = Bid.objects.values('assigned_worker__user__username').annotate(
        processed=Count('id'),
        avg_completion_time=Avg(
            ExpressionWrapper(
                F('updated_at') - F('created_at'),
                output_field=DurationField()
            )
        )
    ).order_by('-processed')
    return efficiency
