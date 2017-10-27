from django.contrib import admin
from .models import Team, Service, Portifolio


class TeamAdmin(admin.ModelAdmin):

	list_display = ['name', 'slug']
	search_fields = ['name', 'slug']
	prepopulated_fields = {'slug': ['name']}


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

