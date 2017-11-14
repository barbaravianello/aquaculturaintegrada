from django.contrib import admin
from .models import Team, Service, Portfolio, PortfolioImage


class TeamAdmin(admin.ModelAdmin):

	list_display = ['name', 'slug']
	search_fields = ['name', 'slug']
	prepopulated_fields = {'slug': ['name']}


class ServiceAdmin(admin.ModelAdmin):

	list_display = ['name', 'slug']
	search_fields = ['name', 'slug']
	prepopulated_fields = {'slug': ['name']}

class PortfolioImageInline(admin.TabularInline):
    model = PortfolioImage
    extra = 0

class PortfolioAdmin(admin.ModelAdmin):
	list_display = ['title', 'slug', 'id_item']
	search_fields = ['title', 'slug', 'id_item']
	prepopulated_fields = {'slug': ['title']}
	inlines = [PortfolioImageInline,]

admin.site.register(Team, TeamAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Portfolio, PortfolioAdmin)

