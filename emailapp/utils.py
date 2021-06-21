from django.utils import timezone
from rest_framework.response import Response
from django_AUS.settings import API_TOKEN, WEB_TOKEN

def get_service_name_or_number(from_number=None, from_service=None):
	if from_number:
		services = {
			1:'amazon_SES',
			2: 'google_SMTP',
			3: 'send_grid'
		}
		return services.get(from_number)
	elif from_service:
		services = {
			'amazon_SES':1,
			'google_SMTP':2,
			'send_grid':3
		}
		return services.get(from_service)

def get_localtime():
	return timezone.localtime(timezone.now())


def is_authenticated_to_view_email():
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            token = request.GET.get("TOKEN")
            # return 403 if token is not passed 
            if not token: 
                return Response({"message":'Token is missing !!'},status=403)
            if token not in [API_TOKEN, WEB_TOKEN]:
                return Response({"message":'invalid token !!'},status=403)

            return view_func(request, token==WEB_TOKEN, *args, **kwargs)
        return wrapper_func
    return decorator


def is_authenticated_to_send_email():
    def decorator(view_func):
        def wrapper_func(self, request, *args, **kwargs):
            token = request.POST.get("TOKEN")
            # return 403 if token is not passed 
            if not token: 
                return Response({"message":'Token is missing !!'},status=403)
            if token not in [API_TOKEN, WEB_TOKEN]:
                return Response({"message":'invalid token !!'},status=403)
            return view_func(self, request, token==WEB_TOKEN, *args, **kwargs)
        return wrapper_func
    return decorator
