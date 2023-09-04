from django.shortcuts import render , redirect , HttpResponse
from django.contrib.auth.forms import UserCreationForm 
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login , logout , authenticate

@login_required(login_url='login')
def home_view(request):
   return render(request , 'home.html')

def register_view(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('home')
    else:
      return HttpResponse('Your Credntials did not match try again')
  return render(request , 'register.html' , {'form':UserCreationForm})

def login_view(request):
  if request.method == 'POST':
    print(request.POST)
    uname = request.POST['username']
    upass = request.POST['password']
    user = authenticate(username = uname , password = upass)
    if user is not None:
      login(request , user)
      return redirect('home')
    else:
     return HttpResponse('User Login Credintials did not Match')
  else:
   return render(request , 'login.html' , {'form':LoginForm})

def logout_view(request):
  logout(request)
  return redirect('login')