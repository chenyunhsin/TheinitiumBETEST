from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import logout


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
      
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('employee_page')  # 重定向到員工頁面
    return render(request, 'login.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def employee_page(request):
    return render(request, 'employee_page.html')

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, 'employee_page.html')
    else:
        form = CustomUserCreationForm()
    return render(request, "register.html", {"form": form})