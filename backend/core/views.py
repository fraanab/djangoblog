from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from posts.models import Post, Comment #models
from .models import Contact, Newsletter, HtmlTemplates #models
from django.contrib.auth import login #login django
from .forms import SignUpForm, NewPost, ContactForm, HtmlTemplatesForm #forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password #edit my account
from django.core.mail import send_mail #newsletter
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def newsletterinfo(request):
	if request.method == 'POST':
		email = request.POST.get('email')
		Newsletter.objects.create(subscribedmail=email)
		return redirect('/')

@login_required
def sendnewsletter(request):
	if request.user.is_superuser:
		subscribers = Newsletter.objects.all()
		subject = 'Blog Newsletter'
		# body = render_to_string('newsletterA.html', {})

		htmltemplate = HtmlTemplates.objects.latest('id')
		body = render_to_string(f'{htmltemplate.template}', {})
		plain_message = strip_tags(body)

		if request.method == 'POST':
			for subscriber in subscribers:
				send_mail(
						f'{subject}',
						f'{plain_message}',
						settings.EMAIL_HOST_USER,
						[f'{subscriber.subscribedmail}'],
						html_message=body,
						fail_silently=False,
					)
			print(body)
		# return render(request, 'sendnewsletter.html', {'subscribers':subscribers})
		return redirect('admin_dashboard')
	else:
		return redirect('/')

def frontpage(request):
	posts = Post.objects.all()
	return render(request, 'frontpage.html', {'posts':posts})

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('contact')
	else:
		form = ContactForm()
	return render(request, 'contact.html', {'form':form})

def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect('/')
	else:
		form = SignUpForm()
	return render(request, 'signup.html', {'form':form})

@login_required
def myaccount(request):
	comments = Comment.objects.filter(user=request.user)
	if request.method == 'POST':
		commenttext = request.POST.get('commenttext')
		Comment.objects.filter(text=commenttext).delete()
		return redirect('myaccount')
	context = {
		'comments': comments
	}
	return render(request, 'myaccount.html', context)

@login_required
def edit_myaccount(request):
	if request.method == 'POST':
		user = request.user
		user.email = request.POST.get('email')
		user.username = request.POST.get('username')
		confirmation = request.POST.get('confirmation')
		if check_password(confirmation, user.password):
			redirect('edit_myaccount')
		else:
			user.save()
			return redirect('myaccount')
	return render(request, 'edit_myaccount.html')

@login_required
def admin_dashboard(request):
	if request.user.is_superuser:
		mails = Contact.objects.all()
		mails_count = mails.count()
		newslettersubs = Newsletter.objects.all()
		newslettersubs_total = newslettersubs.count()
		posts = Post.objects.all()
		totalposts = posts.count()
		htmlform = HtmlTemplatesForm()
		post_form = NewPost()

		if request.method == 'POST':
			post_title = request.POST.get('posttitle')
			Post.objects.filter(title=post_title).delete()
			return redirect('admin_dashboard')

		return render(request, 'admin_dashboard.html', {'post_form':post_form, 'totalposts':totalposts, 'posts': posts, 'mails': mails, 'mails_count':mails_count, 'newslettersubs':newslettersubs, 'newslettersubs_total':newslettersubs_total, 'htmlform':htmlform})
	else:
		return redirect('myaccount')

@login_required
def newpost(request):
	if request.user.is_superuser:
		if request.method == 'POST':
			post_form = NewPost(request.POST, request.FILES)
			if post_form.is_valid():
				new_post = post_form.save(commit=False)
				new_post.slug = new_post.title.replace(" ", "-")
				new_post.image = request.FILES.get('image')
				new_post.save()
				return redirect('admin_dashboard')
			else:
				post_form = NewPost()
	else:
		return redirect('/')

@login_required
def newhtml(request):
	if request.user.is_superuser:
		if request.method == 'POST':
			form = HtmlTemplatesForm(request.POST, request.FILES)
			if form.is_valid():
				new_html = form.save(commit=False)
				new_html.template = request.FILES.get('template')
				new_html.save()
				return redirect('admin_dashboard')
			else:
				return redirect('/')
		else:
			form = HtmlTemplatesForm()
	else:
		return redirect('/')