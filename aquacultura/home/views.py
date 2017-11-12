from django.shortcuts import render, get_object_or_404
from .forms import LeadForm
from django.contrib import messages
from home.models import Team, Service, Portfolio, PortfolioImage
from home.forms import ContactAquacultura


def index(request):
	teams = Team.objects.all()
	portfolios = Portfolio.objects.all()
	
	context = {
		'teams': teams,
		'portfolios': portfolios,
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


def portfolio(request):
	portfolio = Portfolio.objects.all()
	context = {}
	context['portfolio'] = portfolio
	template_name = 'portfolio.html'
	return render(request, template_name, context)
