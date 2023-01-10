from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.core.files import File
from cloudinary.models import CloudinaryField
from io import BytesIO
from PIL import Image

STATUS = (
	(0, "Draft"),
	(1, "Publish")
)


class Post(models.Model):
  thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
  # image = CloudinaryField('image', null=True, blank=True)
  # thumbnail = CloudinaryField('image', null=True, blank=True)
  title = models.CharField(max_length=200, unique=True)
  slug = models.SlugField(max_length=200, unique=True)
  content = RichTextField(null=True, blank=True)
  # author = models.CharField(max_length=100)
  author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts', blank=True, null=True)
  status = models.IntegerField(choices=STATUS, default=1)
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)
  upvotes = models.IntegerField(default=0)

  class Meta:
    ordering = ['-created_on',]
  def __str__(self):
    return self.title

class Comment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
	post_commented = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
	text = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True)
	active = models.BooleanField(default=False)
	def __str__(self):
		return f'Comment by {self.user} on {self.post_commented}'