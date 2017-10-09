from django.db import models

class Team(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Atalho')
    job = models.CharField('Cargo', max_length=100, blank=True)
    description = models.TextField('Descrição ', blank = True)
    image = models.ImageField(upload_to='team/images', verbose_name="Imagem", null=True, blank=True)
    prepopulated_fields = {'slug': ['name']}

    def __str__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('home:details', (), {'slug': self.slug})

    class Meta:
        verbose_name = 'Equipe'
        verbose_name_plural = 'Equipe'
        ordering = ['name']
<<<<<<< HEAD
# Create your models here.
=======


class Service(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Atalho')
    description = models.TextField('Descrição ', blank = True)
    image = models.ImageField(upload_to='team/images', verbose_name="Imagem", null=True, blank=True)
    prepopulated_fields = {'slug': ['name']}

    def __str__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('home:details', (), {'slug': self.slug})

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'
        ordering = ['name']


class Portifolio(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Atalho')
    description = models.TextField('Descrição ', blank = True)
    image = models.ImageField(upload_to='team/images', verbose_name="Imagem", null=True, blank=True)
    prepopulated_fields = {'slug': ['name']}

    def __str__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('home:details', (), {'slug': self.slug})

    class Meta:
        verbose_name = 'Portifólio'
        verbose_name_plural = 'Portifólios'
        ordering = ['name']
>>>>>>> origin/master
