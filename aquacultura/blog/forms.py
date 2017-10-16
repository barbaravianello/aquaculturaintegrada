#-*- coding: utf-8 -*-
from django import forms
from .models import Email
from django.core.mail import send_mail
from django.conf import settings

# Cria o formulario para recolher o e-mail do usuario
class LeadForm(forms.Form):
   name = forms.CharField(max_length = 100, widget=forms.TextInput(attrs={'placeholder': 'Seu nome'}))
   email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'seu.email.aqui@porfavor.com'}))
   email.clean('email@example.com')

   def save_contact(self):
        email = Email(nome=self.cleaned_data['name'], email=self.cleaned_data['email'])
        email.save()
        # envio de mensagem de boas vindas
        message = "Olá %s,\nObrigado por se cadastrar para receber as novidades do nosso blog. Estaremos sempre disponível para qualquer dúvida.\n\nFavor não responder este email." %(email.nome)

        send_mail('Confirmação de envio - Blog Aquacultura', message,
            settings.DEFAULT_FROM_EMAIL, [email.email])

   def __str__(self):
        return self.name
