from django.shortcuts import render, redirect
from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print('Saving User')

            return redirect('dash')
    else:
        form = UserRegistrationForm()

    return render(request, 'users/register.html',
                  {'form': form})
