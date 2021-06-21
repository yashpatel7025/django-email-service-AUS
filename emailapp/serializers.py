from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import *
from .utils import get_service_name_or_number

class EmailSerializer(ModelSerializer):
	status = SerializerMethodField()
	sent_via = SerializerMethodField()
	class Meta:
		model = Email
		fields = ('id', 'from_email', 'to_email','subject', 'body_text','sent_via', 'created', 'status')

	def get_status(self, obj):
		return "sent" if obj.status else "failed"

	def get_sent_via(self, obj):
		return get_service_name_or_number(from_number=obj.sent_via)
