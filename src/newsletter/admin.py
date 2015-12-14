from django.contrib import admin
from django_markdown.admin import MarkdownModelAdmin

# Register your models here.
from .forms import SignUpForm

from .models import SignUp, Level, UserProfile

class SignUpAdmin(admin.ModelAdmin):
	list_display=["__unicode__","timestamp","updated"]
	form=SignUpForm
	#class Meta:
		#model=SignUp

# class levelAdmin(MarkdownModelAdmin):
# 	list_display=("level_number","question")

class UserProfileAdmin(admin.ModelAdmin):
	list_display=["user","current_level","time"]

admin.site.register(SignUp,SignUpAdmin)
admin.site.register(Level,MarkdownModelAdmin)
admin.site.register(UserProfile,UserProfileAdmin)
