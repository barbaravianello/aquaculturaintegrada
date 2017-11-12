from django.contrib import admin
from .models import Team, Service, Portifolio, PortifolioImage


class TeamAdmin(admin.ModelAdmin):

	list_display = ['name', 'slug']
	search_fields = ['name', 'slug']
	prepopulated_fields = {'slug': ['name']}


class ServiceAdmin(admin.ModelAdmin):

	list_display = ['name', 'slug']
	search_fields = ['name', 'slug']
	prepopulated_fields = {'slug': ['name']}

class PortifolioImageInline(admin.TabularInline):
    model = PortifolioImage
    extra = 0

class PortifolioAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	search_fields = ['name', 'slug']
	prepopulated_fields = {'slug': ['name']}
	inlines = [PortifolioImageInline,]

admin.site.register(Team, TeamAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Portifolio, PortifolioAdmin)

