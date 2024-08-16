from django.template import Template, Context
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView, DetailView
from django.urls import reverse_lazy
from .models import Contacto, Disco
from django.http import HttpResponse
from django.urls import get_resolver
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView
from django.db import models
from django.db.models import Q
from .forms import DiscoForm
from django.contrib import messages

def show_urls(request):
    urls = get_resolver().reverse_dict.keys()
    urls_list = "\n".join([str(url) for url in urls])
    return HttpResponse(f"<pre>{urls_list}</pre>")

@login_required
def home(request):
    return render(request, "home.html", {})
    
def authView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})

def template(request):
    return render(request, 'base.html')


def resultados(request):
    nombre = request.GET.get('nombre', '')
    resultados = Cliente.objects.filter(nombre__icontains=nombre)
    context = {'nombre': nombre, 'resultados': resultados}
    return render(request, 'resultados.html', context)


def contact_submit(request):
    if request.method == "POST":
        nombre = request.POST.get('name')
        email = request.POST.get('email')
        telefono = request.POST.get('phone')
        mensaje = request.POST.get('message')

        nuevo_contacto = Contacto(nombre=nombre, email=email, telefono=telefono, mensaje=mensaje)
        nuevo_contacto.save()

        messages.success(request, '¡Gracias por contactarnos! Te responderemos pronto.')

        return redirect('/#contact')
    return redirect('/#contact')


class AdminView(UserPassesTestMixin, CreateView):
    model = Disco
    template_name = 'adminview.html'
    form_class = DiscoForm
    success_url = reverse_lazy('admin_view')

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.groups.filter(name='Admin').exists()

    def handle_no_permission(self):
        return redirect('/accounts/login/')
    
    def form_valid(self, form):
        messages.success(self.request, 'El disco ha sido cargado correctamente.')
        return super().form_valid(form)

@login_required
def buscar(request):
    nombre = request.GET.get('nombre')
    resultados = []
    if nombre:
        resultados = Disco.objects.filter(
            Q(titulo__icontains=nombre) |
            Q(interprete__icontains=nombre) |
            Q(genero__icontains=nombre)
        )
    return render(request, 'buscar.html', {'nombre': nombre, 'resultados': resultados})

def is_admin(user):
    return user.is_authenticated and user.is_superuser

@user_passes_test(is_admin, login_url='/accounts/login/')
def admin_view(request):
    if request.method == 'POST':
        form = DiscoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'El disco ha sido cargado correctamente.')
            return redirect('admin_view') 
    else:
        form = DiscoForm()

    return render(request, 'adminview.html', {'form': form})

class ListaDiscosView(LoginRequiredMixin, ListView):
    model = Disco
    template_name = 'lista.html'
    context_object_name = 'discos'
    login_url = '/accounts/login/'

class EditarDiscoView(UserPassesTestMixin, UpdateView):
    model = Disco
    form_class = DiscoForm
    template_name = 'editar_disco.html'
    success_url = reverse_lazy('lista')

    def test_func(self):
        return self.request.user.is_superuser

    def form_valid(self, form):
        messages.success(self.request, 'El disco ha sido actualizado correctamente.')
        return super().form_valid(form)

class BorrarDiscoView(UserPassesTestMixin, DeleteView):
    model = Disco
    template_name = 'borrar_disco.html'
    success_url = reverse_lazy('lista')

    def test_func(self):
        return self.request.user.is_superuser

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'El disco ha sido eliminado correctamente.')
        return super().delete(request, *args, **kwargs)

class DiscoDetailView(DetailView):
    model = Disco
    template_name = 'disco_detalle.html'
    context_object_name = 'disco'
