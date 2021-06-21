from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
	
    path('view_sent_emails/', views.get_email_list, name='sent_emails_list_view'),
    path('send_email/', views.EmailAPIView.as_view(), name='send_email'),
    path('', views.redirect_home, name="redirect_home"),
     
] 