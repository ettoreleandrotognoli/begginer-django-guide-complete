from django.db import models
from django.utils.text import Truncator

# Create your models here.

from django.contrib.auth.models import User

class Board(models.Model):
	name = models.CharField(max_length=30, unique=True)
	description = models.CharField(max_length=100)

	def __str__(self):
		return self.name

	def get_posts_count(self):
		return Post.objects.filter(topic__board=self).count()

	def get_last_post(self):
		return Post.objects.filter(topic__board=self).order_by('-created_at').first()

class Topic(models.Model):
	subject = models.CharField(max_length=255)
	last_updated = models.DateTimeField(auto_now_add=True)
	board = models.ForeignKey(Board, related_name='topics')
	starter = models.ForeignKey(User, related_name='topics')
	views = models.PositiveIntegerField(default=0)

	def __str__(self):
		return self.subject

class Post(models.Model):
	message = models.TextField(max_length=4000)
	topic = models.ForeignKey(Topic, related_name='posts')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(null=True)
	created_by = models.ForeignKey(User, related_name ='posts')
	updated_by = models.ForeignKey(User, null=True, related_name='+')

	def __str__(self):
		truncated_message = Truncator(self.message)
		return truncated_message.chars(30)

# we are using the Truncator utility class. It’s a convenient way to truncate long 
# strings into an arbitrary string size (here we are using 30).

# All models are subclass of the django.db.models.Model class
# Each class will be transformed into database tables.
# Each field is represented by instances of django.db.models.Field 
# subclasses (built-in Django core) and will be translated into database columns.

# In he Post model, the updated_by field sets the related_name='+'. 
# This instructs Django that we don’t need this reverse relationship, so it will ignore it.

# If we don’t specify a primary key for a model, Django will automatically generate it for us