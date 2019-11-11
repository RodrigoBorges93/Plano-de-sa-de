from django.shortcuts import render, redirect
from .models import Usuario
from django.contrib import messages
from django.views.generic.edit import CreateView
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect



def home(request):
    return render(request, 'main/index.html')

class Criar_usuario(CreateView):
  model = Usuario
  fields = ['nome', 'plano', 'email','telefone']

  def form_valid(self, form):
    usuario = form.save(commit = False)
    usuario.save()
    return redirect('https://www.google.com/')

