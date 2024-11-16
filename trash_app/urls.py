# from django.urls import path
# from . import views
# from django.http import HttpResponse
# from django.contrib.auth.views import LoginView, LogoutView
#
#
# def debug_user_info(request):
#     if request.user.is_authenticated:
#         return HttpResponse(f"Logged in as: {request.user.username}")
#     else:
#         return HttpResponse("Not logged in.")
#
# urlpatterns = [
#     path('trash_can/new', views.create_trash_can, name='create_trash_can'), # create trash can
#     path('trash_can/list', views.list_trash_cans, name='list_trash_cans'), # list trash cans
#
#     path('bid/new/<int:trash_can_id>', views.create_bid, name='create_bid'), # create bid
#     path('bid/list', views.list_bids, name='list_bids'), # list bids
#
#     path('me/', debug_user_info, name='debug_user_info'), # debug user info
#
#     path('register/', views.register, name='register'), # register
#     path('login/', LoginView.as_view(template_name='login.html'), name='login'), # login
#     path('logout/', LogoutView.as_view(), name='logout'), # logout
# ]
#
