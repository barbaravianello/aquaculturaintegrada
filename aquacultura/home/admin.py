from django.contrib import admin
<<<<<<< HEAD
from .models import Team
=======
from .models import Team, Service, Portifolio

>>>>>>> origin/master

class TeamAdmin(admin.ModelAdmin):

	list_display = ['name', 'slug']
	search_fields = ['name', 'slug']
	prepopulated_fields = {'slug': ['name']}

<<<<<<< HEAD
admin.site.register(Team, TeamAdmin)
=======

class ServiceAdmin(admin.ModelAdmin):

	list_display = ['name', 'slug']
	search_fields = ['name', 'slug']
	prepopulated_fields = {'slug': ['name']}


class PortifolioAdmin(admin.ModelAdmin):
	
	list_display = ['name', 'slug']
	search_fields = ['name', 'slug']
	prepopulated_fields = {'slug': ['name']}


admin.site.register(Team, TeamAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Portifolio, PortifolioAdmin)
>>>>>>> origin/master

