from django import forms
from blog.models import Email
from django.core.mail import send_mail
from django.conf import settings 

class ContactAquacultura(forms.Form):

	name = forms.CharField(label = 'Nome', widget=forms.TextInput(attrs={'class':'form-control', 'required':'required'}))
	lastname = forms.CharField(label = 'Sobrenome', widget=forms.TextInput(attrs={'class':'form-control','required':'required'}))
	email = forms.EmailField(label = 'E-mail', widget=forms.TextInput(attrs={'class':'form-control','required':'required', 'type': 'email'}) )
	phone = forms.IntegerField(label='Telefone', widget=forms.TextInput(attrs={'class':'form-control','required':'required', 'type': 'phone'}))
	message = forms.CharField(label='Mensagem', widget=forms.Textarea(attrs={'class':'form-control', 'rows': 10, 'cols': 30, 'required':'required'}))


	def send_mail(self):
		message = '--------------------------------------------------------------------------------\n'
		message += ' [CONTATO - SITE] Novo email de contato no site Aquacultura \n'
		message += '--------------------------------------------------------------------------------\n'
		message += 'NOME: %(name)s' + ' %(lastname)s \n'
		message += 'E-MAIL: %(email)s \n'
		message += 'TELEFONE: %(phone)s \n'
		message += 'MENSAGEM: %(message)s \n'


		context = {
			'name': self.cleaned_data['name'],
			'lastname': self.cleaned_data['lastname'],
			'email': self.cleaned_data['email'],
			'phone': self.cleaned_data['phone'],
			'message': self.cleaned_data['message'],

		}
		subject = "Novo e-mail de contato no site Aquacultura"
		message = message % context
		send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.CONTACT_EMAIL])


# Cria o formulario para recolher o e-mail do usuario
class LeadForm(forms.Form):
   name = forms.CharField(label = "Nome", max_length = 100, widget=forms.TextInput())
   email = forms.EmailField(label = "E-mail", widget=forms.TextInput())
   email.clean('email@example.com')

   def save_contact(self):
        email = Email(nome=self.cleaned_data['name'], email=self.cleaned_data['email'])
        email.save()
        # envio de mensagem de boas vindas
        message = "Olá %s,\nObrigado por se cadastrar para receber nossas novidades. Estaremos sempre disponível para qualquer dúvida.\n\nFavor não responder este email." %(email.nome)

        send_mail('Confirmação de envio - Blog Aquacultura', message,
            settings.DEFAULT_FROM_EMAIL, [email.email])

   def __str__(self):
        return self.name
