# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return redirect('register_done')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

def register_done(request):
    return render(request, 'accounts/register_done.html')
