from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import WorkerViewSet, BidViewSet, WorkerBidsView

# Create a router and register our viewsets
router = DefaultRouter()
router.register(r'workers', WorkerViewSet, basename='worker')
router.register(r'bids', BidViewSet, basename='bid')

urlpatterns = [
    path('', include(router.urls)),
    path('workers/<int:worker_id>/bids/', WorkerBidsView.as_view(), name='worker-bids'),
]
