from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse

def debug_user_info(request):
    if request.user.is_authenticated:
        return HttpResponse(f"Logged in as: {request.user.username}")
    else:
        return HttpResponse("Not logged in.")

urlpatterns = [
    path('register/', views.register, name='register'),  # register
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),  # login
    path('logout/', LogoutView.as_view(), name='logout'),  # logout
    path('me/', debug_user_info, name='debug_user_info'), # debug user info
]