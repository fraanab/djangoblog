from django.urls import path, include
from core.views import frontpage, signup, myaccount, edit_myaccount, admin_dashboard, contact, newsletterinfo, sendnewsletter, newpost, newhtml, delete
from posts.views import postpage, upvote
from django.contrib.auth import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
	path('', frontpage, name='frontpage'),
	path('newsletter/', newsletterinfo, name='newsletterinfo'),
	path('sendnewsletter/', sendnewsletter, name='sendnewsletter'),
	
	path('newpost/', newpost, name='newpost'),
	path('newhtml/', newhtml, name='newhtml'),
	path('delete/<slug:slug>/', delete, name='delete'),
	path('upvote/<slug:slug>/', upvote, name='upvote'),

	path('signup/', signup, name='signup'),
	path('logout/', views.LogoutView.as_view(), name='logout'),
	path('login/', views.LoginView.as_view(template_name='login.html'), name='login'),
	path('user/', myaccount, name='myaccount'),
    path('user/edit/', edit_myaccount, name='edit_myaccount'),
    path('user/admin/', admin_dashboard, name='admin_dashboard'),
	path('post/<slug:slug>/', postpage, name='postpage'),
	path('contact/', contact, name='contact'),
]