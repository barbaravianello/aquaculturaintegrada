from django.db import models
from django import forms
from django.utils import timezone
from ckeditor.fields import RichTextField
import os
from uuid import uuid4

# ------------ Rename Uploaded Image ----------- #
def path_and_rename(instance, filename):
    upload_to = 'img'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)

# ---------- Models ------------ #

class Categoria(models.Model):
    nome = models.CharField('Nome da categoria',max_length=100)
    slug = models.SlugField('Atalho')
    def __str__(self):
        return self.nome

    @models.permalink
    def get_absolute_url(self):
        return ('blog:category_posts', (), {'slug': self.slug})

class Editor(models.Model):
    nome = models.CharField('Nome e Sobrenome do Editor', max_length=100)
    facebooklink = models.CharField('Link do Facebook pessoal', max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nome


class Post(models.Model):
    editor = models.ManyToManyField(Editor)
    title = models.CharField(max_length=100)
    slug = models.SlugField('Atalho')
    subtitle = models.CharField(max_length=100,null=True, blank=True)
    keywords = models.CharField('Keywords', max_length=150, help_text="Palavras chaves separadas por vírgula", null=True, blank=True)
    capa = models.ImageField('Foto da capa', upload_to=path_and_rename, help_text="Resolução recomendada: 800x600 horizontal", default='blog/img/logo.svg')
    nivel = models.PositiveSmallIntegerField(default=1, null=True)
    categoria = models.ManyToManyField(Categoria)
    content = RichTextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('blog:post_detail', (), {'slug': self.slug})

class Email(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nome
class EnviarEmail(models.Model):
    assunto = models.CharField(max_length=200)
    texto = RichTextField()
