from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def register(request):
    register_form=UserCreationForm()
    return render(request, "user_action/register.html",{"reg_form":register_form})
