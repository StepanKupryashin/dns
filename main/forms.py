from django.contrib.auth.forms import UserCreationForm
from django.forms import * 
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.forms import AuthenticationForm

class RegisterUserForm(UserCreationForm):
    username = CharField(label='Никнейм', widget=TextInput(attrs={'class': 'form-input', 'placeholder': 'Введите никнейм'}))
    email = CharField(label='Email', widget=EmailInput(attrs={'class': 'form-input', 'placeholder': 'Введите email'}))
    password1 = CharField(label='Пароль', widget=PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Введите пароль'}))
    password2 = CharField(label='Повтор пароля', widget=PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Повторить пароль'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widget = {
            'username': TextInput(attrs={'class': 'form-input'}),
            'email': EmailInput(attrs={'class': 'form-input'}),
            'password1': PasswordInput(attrs={'class': 'form-input'}),
            'password2': PasswordInput(attrs={'class': 'form-input'})
        }
class CustomAuthForm(AuthenticationForm):
    username = CharField(widget=TextInput(attrs={'class':'validate','placeholder': 'Логин'}))
    password = CharField(widget=PasswordInput(attrs={'placeholder':'Пароль'}))
