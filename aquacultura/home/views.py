from django.shortcuts import render
from home.models import Team, Service, Portifolio
from home.forms import ContactAquacultura

def index(request):
	teams = Team.objects.all()
	portifolios = Portifolio.objects.all()
	context = {
		'teams': teams,
		'portifolios': portifolios,
	}
	if request.method == 'POST': 
		form = ContactAquacultura(request.POST, request.FILES)
		if form.is_valid():
			context['is_valid'] = True
			form.send_mail()
			form = ContactAquacultura()	
	else:
		form = ContactAquacultura()
	context['form'] = form

	return render(request, "index.html", context)

def service(request):
	services = Service.objects.all()
	context = {
		'services': services,
	}
	return render(request, "services.html", context)

def contact(request):
	return render(request, "contact.html")