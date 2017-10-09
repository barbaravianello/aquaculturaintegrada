from django import forms
from django.core.mail import send_mail
from django.conf import settings 
from home import views


class ContactAquacultura(forms.Form):

	name = forms.CharField(label = 'Nome', widget=forms.TextInput(attrs={'class':'form-group', 'placeholder':'Nome', 'required':'required'}))
	lastname = forms.CharField(label = 'Sobrenome', widget=forms.TextInput(attrs={'class':'form-group', 'placeholder':'Nome', 'required':'required'}))
	email = forms.EmailField(label = 'E-mail', widget=forms.TextInput(attrs={'class':'form-group', 'placeholder':'seuemail@gmail.com', 'required':'required', 'type': 'email'}) )
	phone = forms.IntegerField(label='Telefone', widget=forms.TextInput(attrs={'class':'form-group', 'placeholder':'(84) 3245-2124', 'required':'required', 'type': 'phone'}))
	message = forms.CharField(label='Mensagem', widget=forms.Textarea(attrs={'class':'form-group','placeholder':'Escreva sua mensagem', 'required':'required'}))


	def send_mail(self):
		message = '--------------------------------------------------------------------------------\n'
		message += ' [CONTATO - SITE] Novo email de contato no site MetalPlan \n'
		message += '--------------------------------------------------------------------------------\n'
		message += 'NOME: %(name)s \n'
		message += 'E-MAIL: %(email)s \n'
		message += 'MENSAGEM: %(message)s \n'


		context = {
			'name': self.cleaned_data['name'],
			'email': self.cleaned_data['email'],
			'about': self.cleaned_data['about'],
			'message': self.cleaned_data['message'],

		}

		subject = self.cleaned_data['about']
		message = message % context
		send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.CONTACT_EMAIL])