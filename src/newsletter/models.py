from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django_markdown.models import MarkdownField

class SignUp(models.Model):
	email=models.EmailField()
	full_name=models.CharField(max_length=120,blank=True,null=True)
	timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
	updated=models.DateTimeField(auto_now_add=False,auto_now=True)

	def __unicode__(self):
		return self.email

class Level(models.Model):
	level_number=models.IntegerField(unique=True)
	question=MarkdownField()
	answer=models.CharField(max_length=200)


	def __str__(self):
		return 'Level:%d'% self.level_number


class UserProfile(models.Model):
	user=models.OneToOneField(User, related_name='profile')
	current_level=models.IntegerField(default=1)
	time=models.DateTimeField(auto_now_add=False,auto_now=True)


	def __str__(self):
		return '%s at Level-%d' % (self.user.username,self.current_level)


def create_user_profile(sender,instance,created, **kwargs):
	if created:
		UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile,sender=User)