from django.shortcuts import render
from users.models import User

# Create your views here.

def user_list(request):
    users = User.objects.all()[:3]
    print(users)
    return render(request, 'user_list.html', {'users': users})

def welcome(request):
    return render(request, 'welcome.html')