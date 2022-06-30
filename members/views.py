from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from .forms import RegisterUserForm

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
        else:
            messages.error(request,'username or password not correct')
            return redirect('login')
    else:
        form = AuthenticationForm()
        return render(request, 'registration/login.html', {'form': form})
    
def logout_user(request):
    logout(request)
    
def create_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
			# username = form.cleaned_data['username']
			# password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration Successful!"))
            return redirect('default')
    else:
        form = RegisterUserForm()
    return render(request, 'registration/sign-up.html', {'form':form})
    