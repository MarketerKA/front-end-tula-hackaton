from django.http import HttpResponseForbidden
from functools import wraps

def role_required(allowed_roles):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.profile.role in allowed_roles:
                return view_func(request, *args, **kwargs)
            return HttpResponseForbidden("Access denied.")
        return _wrapped_view
    return decorator