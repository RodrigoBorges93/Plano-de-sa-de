from django.db import models
from phone_field import PhoneField

class Usuario(models.Model):
  nome = models.CharField(max_length = 40, help_text = "Digite seu nome completo")
  tipo_de_plano = [('Individual', 'Individual'), ('Familiar', 'Familiar')]
  plano = models.CharField(max_length = 10, choices = tipo_de_plano, default = 'Individual', help_text = "Escolha entre os dois tipos de plano acima (apenas serve como referência)")
  email = models.EmailField(help_text = 'Obrigatório. Adicione um e-mail para que possamos entrar em contato')
  telefone = PhoneField(help_text = "Digite seu telefone, caso utilize ramal, coloque no campo ext.")

  def __str__ (self):
      return self.nome