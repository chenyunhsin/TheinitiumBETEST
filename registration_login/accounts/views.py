from django.shortcuts import render
from django.contrib.auth import authenticate, login

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