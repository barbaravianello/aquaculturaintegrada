from django.contrib import admin
from .models import Team

class TeamAdmin(admin.ModelAdmin):

	list_display = ['name', 'slug']
	search_fields = ['name', 'slug']
	prepopulated_fields = {'slug': ['name']}

admin.site.register(Team, TeamAdmin)

