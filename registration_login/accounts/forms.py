from django.contrib.auth.forms import UserChangeForm
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser  
        fields = ["username","first_name","last_name","is_employee"]


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser  
        fields =  ["username","password1","password2","is_employee"]