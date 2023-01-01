from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from posts.models import Post
from .models import Contact, HtmlTemplates

class SignUpForm(UserCreationForm):
	email = forms.EmailField(max_length=255, required=True)

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2',]

class NewPost(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['image', 'title', 'content', 'status', 'author',]
		# fields = ['image', 'title', 'status', 'author',]

class UserPost(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['image', 'title', 'content']

class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = ['email', 'message']

class HtmlTemplatesForm(forms.ModelForm):
	class Meta:
		model = HtmlTemplates
		fields = '__all__'