from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Board(models.Model):
	name = models.CharField(max_length=30, unique=True)
	description = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Topic(models.Model):
	subject = models.CharField(max_length=255)
	last_updataed = models.DateTimeField(auto_now_add=True)
	board = models.ForeignKey(Board, related_name='topics')
	starter = models.ForeignKey(User, related_name='topics')

class Post(models.Model):
	message = models.TextField(max_length=4000)
	topic = models.ForeignKey(Topic, related_name='posts')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(null=True)
	created_by = models.ForeignKey(User, related_name ='posts')
	updated_by = models.ForeignKey(User, null=True, related_name='+')

# All models are subclass of the django.db.models.Model class
# Each class will be transformed into database tables.
# Each field is represented by instances of django.db.models.Field 
# subclasses (built-in Django core) and will be translated into database columns.

# In he Post model, the updated_by field sets the related_name='+'. 
# This instructs Django that we don’t need this reverse relationship, so it will ignore it.

# If we don’t specify a primary key for a model, Django will automatically generate it for us