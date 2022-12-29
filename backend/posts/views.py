from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment

def postpage(request, slug):
	post = get_object_or_404(Post, slug=slug)
	posts = Post.objects.all()
	comment = Comment()
	comments = post.comments.filter(active=True)
	newcomment = None

	if request.method == 'POST':
		from_user = request.user
		message = request.POST.get('message')
		active = True
		Comment.objects.create(user=from_user, post_commented=post, text=message, active=active)
		redirect(f'post/{post.slug}')

	context = {
		'post': post,
		'comments': comments,
		'comment': comment,
		'posts': posts
	}
	return render(request, 'post.html', context)