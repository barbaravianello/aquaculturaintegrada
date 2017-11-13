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
    icon = IconField()
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
    name = models.CharField('Nome', max_length=100)
    id_item = models.CharField('Insira o id (1, 2, 3,...) do item desejado', max_length=3, default=1)
    slug = models.SlugField('Atalho')
    main_image = models.ImageField(upload_to='portifolio/images', verbose_name="Imagem", default="{% static'images/port1.png' %}")
    description = models.TextField('Descrição ', blank = True)
    prepopulated_fields = {'slug': ['name']}

    objects = PortfolioManager()
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Portfólio'
        verbose_name_plural = 'Portfólios'
        ordering = ['name']

class PortfolioImage(models.Model):
    title = models.ForeignKey(Portfolio, related_name='images')
    image = models.ImageField(upload_to='portfolio/images', verbose_name="Imagem")


class Gallery(models.Model):
    gallery_id = models.AutoField(primary_key=True)
    title = models.CharField('Nome', max_length=100)
    image = models.ImageField(upload_to='gallery/images', verbose_name="Imagem")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Galeria'
        verbose_name_plural = 'Galerias'
        ordering = ['title']
    