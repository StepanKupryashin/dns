from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from .models import *
from main.forms import *
from django.contrib.auth.decorators import login_required
from django.core.files.base import ContentFile
import os
from django.core.files.storage import default_storage
from django.conf import settings
from docx import Document
from io import BytesIO
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

# Переделать нахуй


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'main/index.html'
    login_url = '/login/'
    redirect_field_name = 'login'
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data()
        context["title"] = 'Главаня'
        context["cpu"] = Components.objects.all().filter(type="Процессор")
        context["gpu"] = Components.objects.all().filter(type="Видеокарта")
        context["mather"] = Components.objects.all().filter(type="Материнская плата")
        context["ram"] = Components.objects.all().filter(type='Оперативная память')
        context["power_block"] = Components.objects.all().filter(type='Блок питания')
        context['hdd'] = Components.objects.all().filter(type="Накопитель")
        context['mouse'] = Components.objects.all().filter(type="Мышка")
        context['keyboard'] = Components.objects.all().filter(type="Клавиатура")
        context['monitor'] = Components.objects.all().filter(type="Монитор")
        return context



class RegisterView(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    def get_context_data(self, **kwargs):
        context = super(RegisterView, self).get_context_data()
        context["title"] = 'Регистрация'
        return context
    def get_success_url(self):
        return reverse('login')

class LoginUserView(LoginView):
    form_class = CustomAuthForm
    template_name = 'main/login.html'
    def get_context_data(self, **kwargs):
        context = super(LoginUserView, self).get_context_data()
        context["title"] = 'Авторизация'
        return context
    def get_success_url(self):
        return reverse('index')

def logout_user(request):
    logout(request)
    return redirect('login')






def get_docx(request):
    text = request.POST['text-docx']
    document = Document()
    text = text.replace('<br>', '\n')
    document.add_paragraph(f"{text}")
    f = BytesIO()
    document.save(f)
    length = f.tell()
    f.seek(0)
    response = HttpResponse(
        f.getvalue(),
        content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    )
    response['Content-Disposition'] = 'attachment; filename=Ваша сборка.docx'
    response['Content-Length'] = length
    return response

def get_sub_components(request):
    mouse = Components.objects.all().filter(type="Мышка")
    keyboard = Components.objects.all().filter(type="Клавиатура")
    monitor = Components.objects.all().filter(type="Монитор")
    return render(request, 'main/sub_components.html', {'mouse': mouse, 'keyboard': keyboard, 'monitor': monitor})