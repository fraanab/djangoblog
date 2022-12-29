from django.contrib import admin
from .models import Post, Comment

class CommentAdmin(admin.ModelAdmin):
	list_display = ('user', 'post_commented', 'text', 'timestamp',)
	list_filter = ('timestamp','post_commented',)
	search_fields = ['user', 'text']

class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'status', 'created_on')
	list_filter = ('status',)
	search_fields = ['title', 'content']
	prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)
admin.site.register(Comment,CommentAdmin)