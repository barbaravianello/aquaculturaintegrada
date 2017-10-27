from django.utils import timezone
from .models import Post, Categoria
from .forms import LeadForm
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.views.generic.list import ListView
import operator
from django.db.models import Q
from functools import reduce


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    categorias = Categoria.objects.all().order_by('nome')
    # Paginação da Página
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 10)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    # Instanciando coletor de e-mails
    context = {'posts': posts, 'categorias': categorias}
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            form.save_contact()
            form = LeadForm()
            messages.add_message(
                request, messages.SUCCESS, 'E-mail registrado com sucesso!')
    else:
        form = LeadForm()
    context['form'] = form
    return render(request, 'blog/blog.html', context)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    categorias = Categoria.objects.all().order_by('nome')
    postssemelhantes = Post.objects.all().filter(categoria__in=categorias, published_date__lte=timezone.now(), nivel__gt=post.nivel - 1).exclude(slug=slug).order_by('nivel')
    posts_semel = []
    for poster in postssemelhantes:
        if poster not in posts_semel:
            posts_semel.append(poster)
    # Instanciando coletor de e-mails
    context = {'post': post, 'categorias': categorias, 'postssemelhantes': posts_semel}
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            form.save_contact()
            form = LeadForm()
            messages.add_message(
                request, messages.SUCCESS, 'E-mail registrado com sucesso!')
    else:
        form = LeadForm()
    context['form'] = form
    return render(request, 'blog/blog-page.html', context)


def category_posts(request, slug):
    categoriaescolhida = get_object_or_404(Categoria, slug=slug)
    posts = Post.objects.all().filter(categoria=categoriaescolhida, published_date__lte=timezone.now()).order_by('-published_date')
    categorias = Categoria.objects.all().order_by('nome')
    # Instanciando coletor de e-mails
    context = {'posts': posts, 'categorias': categorias, 'categoriaescolhida': categoriaescolhida}
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            form.save_contact()
            form = LeadForm()
            messages.add_message(
                request, messages.SUCCESS, 'E-mail registrado com sucesso!')
    else:
        form = LeadForm()
    context['form'] = form
    return render(request, 'blog/blog.html', context)


class BlogListView(ListView):

    model = Post

    def get_context_data(self, **kwargs):
        context = super(BlogListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class BlogSearchListView(BlogListView):
    """
    Display a Blog List page filtered by the search query.
    """
    paginate_by = 10

    def get_queryset(self, request):
        result = super(BlogSearchListView, self).get_queryset()

        query = request.GET.get('q')
        if query:
            query_list = query.split()
            result = result.filter(
                reduce(operator.and_,
                       (Q(title__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(content__icontains=q) for q in query_list))
            )
        return result


def search(request):
    search = BlogSearchListView()
    posts = search.get_queryset(request)
    categorias = Categoria.objects.all().order_by('nome')
    # Paginação da Página
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 10)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    # Instanciando coletor de e-mails
    context = {'posts': posts, 'categorias': categorias}
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            form.save_contact()
            form = LeadForm()
            messages.add_message(
                request, messages.SUCCESS, 'E-mail registrado com sucesso!')
    else:
        form = LeadForm()
    context['form'] = form
    return render(request, 'blog/search_results.html', context)
