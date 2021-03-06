from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from teamwork.apps.profiles.forms import SignUpForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if not form.is_valid():
            return render(request, 'profiles/signup.html',
                          {'form': form})

        else:
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            User.objects.create_user(username=username, password=password,
                                     email=email)
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')

    else:
        return render(request, 'profiles/signup.html',
                      {'form': SignUpForm()})

# Not sure if this is need. Will look into - andgates
@login_required
def view_profile(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'profiles/view_profile.html', {'user': user})
