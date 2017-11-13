from django.contrib import admin
from .models import Team, Service, Portfolio, PortfolioImage, Gallery


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
	list_display = ['name', 'slug', 'id_item']
	search_fields = ['name', 'slug', 'id_item']
	prepopulated_fields = {'slug': ['name']}
	inlines = [PortfolioImageInline,]

class GalleryAdmin(admin.ModelAdmin):

	list_display = ['title', 'gallery_id']
	search_fields = ['title', 'gallery_id']

admin.site.register(Team, TeamAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Gallery, GalleryAdmin)

