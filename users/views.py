from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import  UserRegistertionForm
# from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegistertionForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account for {username} was successfully created.')
            return redirect('home')
    else:
        form = UserRegistertionForm()
    return render(request, 'users/register.html',{'form':form})

