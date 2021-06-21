from django.utils import timezone

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