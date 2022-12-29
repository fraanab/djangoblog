from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.core.files import File
from io import BytesIO
from PIL import Image

STATUS = (
	(0, "Draft"),
	(1, "Publish")
)


class Post(models.Model):
	image = models.ImageField(upload_to='uploads/', blank=True, null=True)
	thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
	title = models.CharField(max_length=200, unique=True)
	slug = models.SlugField(max_length=200, unique=True)
	author = models.ForeignKey(User, on_delete= models.CASCADE, related_name='blog_posts')
	updated_on = models.DateTimeField(auto_now=True)
	content = RichTextField()
	created_on = models.DateTimeField(auto_now_add=True)
	status = models.IntegerField(choices=STATUS, default=0)

	class Meta:
		ordering = ['-created_on',]
	def __str__(self):
		return self.title
	def get_thumbnail(self):
		if self.thumbnail:
			return self.thumbnail.url
		else:
			if self.image:
				self.thumbnail = self.make_thumbnail(self.image)
				self.save()
				return self.thumbnail.url
			else:
				return 'https://via.placeholder.com/240x240x.jpg'
	def make_thumbnail(self, image, size=(300,300)):
		img = Image.open(image)
		img.convert('RGB')
		img.thumbnail(size)
		thumb_io = BytesIO()
		img.save(thumb_io, 'PNG', quality=85)
		thumbnail = File(thumb_io, name=image.name)
		return thumbnail

class Comment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
	post_commented = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
	text = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True)
	active = models.BooleanField(default=False)
	def __str__(self):
		return f'Comment by {self.user} on {self.post_commented}'