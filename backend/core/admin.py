from django.contrib import admin
from .models import Contact, Newsletter, HtmlTemplates

class ContactAdmin(admin.ModelAdmin):
	list_display = ('email', 'message', 'timestamp')
	list_filter = ('timestamp',)
	search_fields = ['email', 'message']

admin.site.register(Contact, ContactAdmin)
admin.site.register(Newsletter)
admin.site.register(HtmlTemplates)