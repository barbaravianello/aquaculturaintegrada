from django.db import models
from fontawesome.fields import IconField
from django.db.models import Q


class Team(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Atalho')
    job = models.CharField('Cargo', max_length=100, blank=True)
    description = models.TextField('Descrição ', blank = True)
    image = models.ImageField(upload_to='team/images', verbose_name="Imagem", null=True, blank=True)
    prepopulated_fields = {'slug': ['name']}

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Equipe'
        verbose_name_plural = 'Equipe'
        ordering = ['name']


class Service(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Atalho')
    description = models.TextField('Descrição ', blank = True)
    icon = models.ImageField(upload_to='service/images', verbose_name="Imagem")
    prepopulated_fields = {'slug': ['name']}

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'
        ordering = ['name']


class PortfolioManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(Q(name__icontains=query)) | Q(description__contains=query)

class Portfolio(models.Model):
    title = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Atalho')
    main_image = models.ImageField(upload_to='portifolio/images', verbose_name="Imagem Principal")
    description = models.TextField('Descrição ', blank = True)
    prepopulated_fields = {'slug': ['name']}

    objects = PortfolioManager()
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Portfólio'
        verbose_name_plural = 'Portfólios'
        ordering = ['title']

class PortfolioImage(models.Model):
    title = models.ForeignKey(Portfolio, related_name='gallery')
    image = models.ImageField(upload_to='portfolio/images', verbose_name="Imagem")


    