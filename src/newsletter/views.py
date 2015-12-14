# from django.core.mail import send_mail 
from datetime import datetime

from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Level, UserProfile
from django.contrib.auth.decorators import login_required

import django
django.setup()

# Create your views here.
def home(request):
	return render(request,"home.html")




@login_required
def display_level(request, level):
    level_object = get_object_or_404(Level, level_number__exact=level)
    current_user = request.user.profile

    if request.method == 'GET':
        if int(current_user.current_level) <= int(level):
            return render(request, 'hackon_level.html', {'level_object': level_object})
        else:
            return HttpResponseRedirect('/level/%d' % current_user.current_level)
    else:
        level_answer = str(level_object.answer)
        user_answer = str(request.POST['answer'])

        if level_answer == user_answer and int(current_user.current_level) == int(level):
            current_user.current_level += 1
            current_user.time=datetime.now()
            current_user.save(update_fields=['current_level','time'])
            return HttpResponseRedirect('/level/%d' % (int(level) + 1))
        return HttpResponseRedirect('/level/%d' % int(level))

@login_required
def display_leaderboard(request):
    users = UserProfile.objects.all().order_by('-current_level')
    return render(request, 'hackon_leaderboard.html', {'users': users})



