from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.cache import cache
from .models import *

@receiver(post_save, sender=Email)
def question__delete_caches_on_create(sender, instance, created, **kwargs):
	cache_name = "get_sent_emails_user_id_" + str(1)
	if(cache_name in cache):
		cache.delete(cache_name)