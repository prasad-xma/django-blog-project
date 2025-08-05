from django.http import HttpResponseForbidden

def roles_required(*required_roles):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            if request.user.is_authenticated and request.user.role == required_roles:
                return view_func(request, *args, **kwargs)
            return HttpResponseForbidden('Sorry, you are not authorized to view this page!')
        return wrapper
    return decorator