
from rest_framework.views import APIView
from .forms import EmailForm
from .models import *
from django.contrib import messages
from django.shortcuts import render, redirect
from rest_framework.response import Response
from .utils import *
from yashi_multi_email_service.impl.EmailManagerService import EmailManagerService
from django_AUS.settings import YASHI_MULTI_EMAIL_SERVICE_CONFIG, API_TOKEN, WEB_TOKEN
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes
from django.core.cache import cache
from rest_framework.pagination import PageNumberPagination
from .serializers import EmailSerializer
from django_AUS import settings
from django.urls import reverse

# Create your views here.
@api_view(['GET'])
def redirect_home(request):
	return redirect(reverse('send_email'))

@api_view(['GET'])
@is_authenticated_to_view_email()
def get_email_list(request, is_from_web):
    cache_name = "get_sent_emails_user_id_" + str(1)
    if(cache_name in cache):
    	#cache hit
        sent_emails = cache.get(cache_name)
    else:
        #cache miss
        sent_emails = Email.objects.all().order_by("-created")
        cache.set(cache_name, sent_emails, timeout=settings.DEFAULT_TIMEOUT)
    paginator = PageNumberPagination()
    page = paginator.paginate_queryset(sent_emails, request)
    if is_from_web:
    	context={
             'emails_sent': page
            }
    	return render(request,'emails_list_view.html',context)
    serialized_data = EmailSerializer(page, many=True).data
    return paginator.get_paginated_response(serialized_data)
    

class EmailAPIView(APIView):

	authentication_classes = []

	@csrf_exempt
	def get(self, request):
		email_form = EmailForm()
		context = {
		        'email_form': email_form,
		    }
		return render(request,'email_form.html',context)

	@csrf_exempt
	@is_authenticated_to_send_email()
	def post(self, request, is_from_web):
		#when form submitted
		email_form = EmailForm(request.POST)
		if email_form.is_valid():
			YASHI_MULTI_EMAIL_SERVICE_CONFIG["DEFAULT_SERVICE"] = get_service_name_or_number(from_number=email_form.cleaned_data['sent_via'])
			context ={
			        "config": YASHI_MULTI_EMAIL_SERVICE_CONFIG,
					"to_email": email_form.cleaned_data['to_email'],
					"subject": email_form.cleaned_data['subject'],
					"body_text": email_form.cleaned_data['body_text']
		      }

			email_manager_service = EmailManagerService()
			sent_via_service, sent_status = email_manager_service.send_email(context)
			email_obj = email_form.save(commit=False) 
			email_obj.status = sent_status
			email_obj.sent_via = get_service_name_or_number(from_service=sent_via_service) if sent_via_service else None
			email_obj.save()
			messages.success(request, f'Email sent successfully')
			if is_from_web:
				return redirect(reverse('sent_emails_list_view') + f"?TOKEN={request.POST['TOKEN']}")
			return JsonResponse({'message':'Email sent successfully',"status": 200})
		#if not valid..return same form with errors
		context={
	         'email_form':email_form
	           }
		if is_from_web:
			return render(request,'email_form.html',context)
		return JsonResponse({'errors':dict(email_form.errors.items()),"status": 400})
		
