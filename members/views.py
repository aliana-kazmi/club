from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        # username = request.POST.get('username')
        # password = request.POST.get('password')
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('search-events')
        else:
            messages.error(request,'username or password not correct')
            return redirect('login')
    else:
        form = AuthenticationForm()
        return render(request, 'registration/login.html', {'form': form})
    