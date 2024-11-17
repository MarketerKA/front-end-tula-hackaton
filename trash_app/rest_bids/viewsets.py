from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from ..models import Bid, Worker
from .serializers import BidSerializer, WorkerSerializer

class WorkerViewSet(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer


class BidViewSet(viewsets.ModelViewSet):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer

    # Assign a worker to a bid
    @action(detail=True, methods=['post'])
    def assign_worker(self, request, pk=None):
        bid = self.get_object()
        worker_id = request.data.get('worker_id')
        try:
            worker = Worker.objects.get(id=worker_id)
            bid.assigned_worker = worker
            bid.status = 'in_progress'
            bid.save()
            return Response({
                'message': f"Worker {worker.user.username} assigned to bid {bid.id}.",
                'bid': BidSerializer(bid).data
            }, status=status.HTTP_200_OK)
        except Worker.DoesNotExist:
            return Response({'error': 'Worker not found'}, status=status.HTTP_404_NOT_FOUND)

    # Mark a bid as completed
    @action(detail=True, methods=['post'])
    def mark_completed(self, request, pk=None):
        bid = self.get_object()
        bid.status = 'completed'
        bid.save()
        return Response({
            'message': f"Bid {bid.id} marked as completed.",
            'bid': BidSerializer(bid).data
        }, status=status.HTTP_200_OK)
