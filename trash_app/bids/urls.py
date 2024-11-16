from django.urls import path
from . import views

urlpatterns = [
    path('list', views.bid_list, name='bid_list'),  # List all bids
    path('create', views.create_bid, name='create_bid'),  # Create new bid
    path('<int:bid_id>/', views.bid_detail, name='bid_detail'),  # Detail view for a bid
    path('<int:bid_id>/update/', views.update_bid, name='update_bid'),  # Update bid
    path('<int:bid_id>/delete/', views.delete_bid, name='delete_bid'),  # Delete bid
    path('assign/<int:bid_id>/<int:worker_id>', views.assign_bid_to_worker, name='assign_bid_to_worker'),
    path('workers/list', views.worker_list, name='worker_list'),  # List all workers
    path('workers/create', views.create_worker_view, name='create_worker'),  # Create new worker
    path('workers/<int:worker_id>/bids/', views.worker_bids, name='worker_bids'),
]
