from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os

class Contact(models.Model):
	email = models.EmailField(max_length=255)
	message = models.TextField(max_length=255)
	timestamp = models.DateTimeField(auto_now_add=True)
	class Meta:
		verbose_name_plural = 'Contact Page'
	def __str__(self):
		return f'Message sent by {self.email}'

class Newsletter(models.Model):
	subscribedmail = models.EmailField(max_length=255)
	timestamp = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return f'{self.subscribedmail} subscribed {self.timestamp}'

uploadpath = FileSystemStorage(location=os.path.join(settings.BASE_DIR, 'core/templates', '') )

class HtmlTemplates(models.Model):
	template = models.FileField(storage=uploadpath, blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True)