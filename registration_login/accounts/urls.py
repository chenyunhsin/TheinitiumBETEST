from django.urls import path
from .views import employee_page
from . import views
urlpatterns = [
    # 其他 URL 映射...
    path('', employee_page, name='employee_page'),
    path('logout/', views.user_logout, name='logout'),
    path('login/', views.user_login, name='login'),
    path("register/", views.register, name="register"),
]
