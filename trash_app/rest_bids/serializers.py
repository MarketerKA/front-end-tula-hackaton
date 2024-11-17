from rest_framework import serializers
from ..models import Bid, Worker

class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = ['id', 'user', 'image_before', 'datetime_image_before', 'location_image_before',
                  'image_after', 'datetime_image_after', 'location_image_after']


class BidSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source='get_type_display', read_only=True)
    status = serializers.CharField(source='get_status_display', read_only=True)
    worker_id = serializers.IntegerField(source='assigned_worker.id', read_only=True)
    class Meta:
        model = Bid
        fields = ['id', 'type', 'coordinates',
                  'image', 'description', 'status',
                  'created_at', 'worker_id']
