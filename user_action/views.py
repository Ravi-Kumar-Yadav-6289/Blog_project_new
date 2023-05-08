from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        register_form = UserCreationForm(request.POST)
        if register_form.is_valid():
            username=register_form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}!")
            return redirect('blog_home')

    else:
        register_form=UserCreationForm()
    return render(request, "user_action/register.html",{"reg_form":register_form})
