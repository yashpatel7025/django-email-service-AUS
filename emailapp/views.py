
from rest_framework.views import APIView
from .forms import EmailForm
from .models import *
from django.contrib import messages
from django.shortcuts import render, redirect
from rest_framework.response import Response
from .utils import get_service_name_or_number
from yashi_multi_email_service.impl.EmailManagerService import EmailManagerService
from django_AUS.settings import YASHI_MULTI_EMAIL_SERVICE_CONFIG
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
# Create your views here.

def get_email_list(request):
	context={
	         'emails_sent': Email.objects.all().order_by("-created")
	         }
	return render(request,'emails_list_view.html',context)

class EmailAPIView(APIView):

	authentication_classes = []

	@csrf_exempt
	def get(self, request, id=None):
		email_form = EmailForm()
		context = {
		        'email_form': email_form,
		    }
		return render(request,'email_form.html',context)

	@csrf_exempt
	def post(self, request):
		#when form submitted
		is_from_outside_app = YASHI_MULTI_EMAIL_SERVICE_CONFIG.get("API_TOKEN") == request.POST.get("API_TOKEN")
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
			if is_from_outside_app:
				return JsonResponse({'message':'Email sent successfully',"status": 200})
			return redirect('sent_emails_list_view')
		#if not valid..return same form with errors
		context={
	         'email_form':email_form
	           }
		if is_from_outside_app:
			return JsonResponse({'errors':dict(email_form.errors.items()),"status": 400})
		return render(request,'email_form.html',context)
		
