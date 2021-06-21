from django.db import models
from .utils import get_localtime

class Email(models.Model):

	class AvailabelService(models.IntegerChoices):
		amazon_SES = 1, "Amazon SES"
		google_SMTP = 2, "Google SMTP"
		send_grid = 3, "SendGrid"

	from_email = models.EmailField("From Email", max_length=100, null=False, blank=False)
	to_email = models.EmailField("To Email", max_length=100, null=False, blank=False)
	subject = models.CharField("Subject", max_length=300, null=False, blank=False)
	body_text = models.TextField("Body Text", max_length=5000, null=False, blank=False)
	sent_via = models.IntegerField(choices=AvailabelService.choices, null=True, blank=True, default=AvailabelService.amazon_SES)
	created = models.DateTimeField(default=get_localtime)
	status = models.BooleanField(default=True, null=False, blank=False)

	def __str__(self):
		return "Email Object sent to " + self.to_email