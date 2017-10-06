from django.shortcuts import render
from home.models import Team

def index(request):
	teams = Team.objects.all()
	context = {
		'teams': teams,
	}
	return render(request, "index.html", context)