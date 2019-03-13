from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

# Create your views here.

def register(request):

	if request.method == 'POST':				## if POST request, then instantiate user form with POST data

		form = UserRegisterForm(request.POST)

		if form.is_valid():

			form.save()

			username = form.cleaned_data.get('username')

			messages.success(request, f'Account created for {username}. You are now able to log in.')

			return redirect('login')

	else:

		form = UserRegisterForm()

	return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
	return render(request, 'users/profile.html')




## types of messages w/ django
	# messages.debug
	# messages.info
	# messages.success
	# messages.warning
	# messages.error 
