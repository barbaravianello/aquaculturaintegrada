from django.shortcuts import render, get_object_or_404
from .forms import LeadForm
from django.contrib import messages
from home.models import Team, Service, Portfolio, PortfolioImage, Gallery
from home.forms import ContactAquacultura

def index(request):
	teams = Team.objects.all()
	galleries = Gallery.objects.all()
	port = Portfolio.objects.all()
	context = {
		'teams': teams,
		'galleries': galleries,
		'port': port,
	}
	if request.method == 'POST':
		form = LeadForm(request.POST)
		if form.is_valid():
			context['is_valid'] = True
			form.save_contact()
			form = LeadForm()
			messages.add_message(request, messages.SUCCESS, 'E-mail registrado com sucesso!')
	else:
		form = LeadForm()
	context['form'] = form
	return render(request, "index.html", context)


def service(request):
	services = Service.objects.all()
	context = {
		'services': services,
	}
	return render(request, "services.html", context)

def galeria(request):
	port = Portfolio.objects.all()
	context = {
		'port': port,
	}
	return render(request, "portfolio.html", context)

def contact(request):
	context = {}
	if request.method == 'POST': 
		form = ContactAquacultura(request.POST or None)
		if form.is_valid():
			context['is_valid'] = True
			form.send_mail()
			form = ContactAquacultura()	
	else:
		form = ContactAquacultura()
	context['form'] = form
	return render(request, "contact.html", context)


def details(request, slug):
	portfolio = get_object_or_404(Portfolio, slug=slug)
	context = {}
#	if request.method == 'POST':
#		form = ContactCourse(request.POST)
#		if form.is_valid():
#			context['is_valid'] = True
#			print(form.cleaned_data['name'])
#			print(form.cleaned_data['email'])
#			print(form.cleaned_data['message'])
#			form.send_mail(course)
#			form =  ContactCourse()
#	else:
#		form = ContactCourse()
#	context['form'] = form
	context['portfolio'] = portfolio
	template_name = 'portfolio.html'
	return render(request, template_name, context)
