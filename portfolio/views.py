from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .models import Semestre
from .models import *
from .forms import Tarefa, SemestreForm, ComentarioForm
from .forms import TarefaForm
from django.contrib.auth.models import User
import requests
from django.shortcuts import render
import datetime

def base_view(request):
    return render(request, 'portfolio/base.html')


def home_view(request):
    return render(request, 'portfolio/home.html')


def contacto_view(request):
    return render(request, 'portfolio/contacto.html')


def projetos_view(request):
    return render(request, 'portfolio/projetos.html')


def blog_view(request):
    return render(request, 'portfolio/blog.html')


def semestre_view(request):
    semestre = Semestre.objects.all()
    context = {'semestre': semestre}
    return render(request, 'portfolio/sobre.html', context)



def home_page_view(request):
    tarefas = Tarefa.objects.all()
    context = {'tarefas': sorted(tarefas, key=lambda tarefa: tarefa.prioridade, reverse=True)}
    return render(request, 'portfolio/blog.html', context)
def edita_Artigo_View(request, tarefa_id):
    tarefa = Tarefa.objects.get(id=tarefa_id)

    form = TarefaForm(request.POST or None, instance=tarefa)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {'form': form, tarefa_id: tarefa_id}
    return render(request, 'portfolio/blog/editaArtigo.html', context)

def criaArtigo(request):
    form = TarefaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('portfolio:blog')

    context = {'form': form}
    return render(request, 'portfolio/blog/criaArtigo.html', context)


def apaga_Artigo_View(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, pk=tarefa_id)

    if request.method == 'POST':
        tarefa.delete()
        return HttpResponseRedirect(reverse('portfolio:blog'))
    return render(request, 'portfolio/blog/apagaArtigo.html', {tarefa: tarefa})


def novoComentario_View(request):
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('portfolio:blog'))
    else:
        form = ComentarioForm()
    comentarios = Comentario.objects.all()

    context = {'form': form,'comentarios': comentarios}
    return render(request, 'portfolio/blog/novoComentario.html', context)

def apagaComentario_View(request, comentario_id):
    comentario =get_object_or_404(Comentario, pk=comentario_id)
    if request.method == 'POST':
            comentario.delete()
            return HttpResponseRedirect(reverse('portfolio:blog'))
    return HttpResponseRedirect(reverse('portfolio:blog'))




def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    return render(request, 'portfolio/user.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('portfolio:user'))
        else:
            return render(request, "portfolio/login.html",
                          {'message': "Credenciais Invalidas!!!"})
    return render(request, 'portfolio/login.html')


def logout_view(request):
    logout(request)
    return redirect('portfolio:login')


def user_view(request):
    return render(request, 'portfolio/user.html')



@login_required
def cadastraSemestre(request):
    form = SemestreForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:sobre'))

    context = {'form': form}
    return render(request, 'portfolio/cadastraSemestre.html', context)


def render_semestre_view(request):
    semestre1 = Semestre.objects.filter(semestre=1)
    semestre2 = Semestre.objects.filter(semestre=2)
    semestre3 = Semestre.objects.filter(semestre=3)
    semestre4 = Semestre.objects.filter(semestre=4)
    semestre5 = Semestre.objects.filter(semestre=5)
    semestre6 = Semestre.objects.filter(semestre=6)

    context = {
        'semestre1': semestre1,
        'semestre2': semestre2,
        'semestre3': semestre3,
        'semestre4': semestre4,
        'semestre5': semestre5,
        'semestre6': semestre6,
    }
    print(context)
    return render(request, 'portfolio/sobre.html', context)



def indexApi_View(request):

    if 'city' in request.POST:
        city = request.POST['city']
    else: city= 'lisbon'
    appid = 'b346afff952cc7c34ec0095cabcd5b99'
    URL = 'http://api.openweathermap.org/data/2.5/weather'
    PARAMS = {'q': city, 'appid': appid, 'units': 'metric'}
    r = requests.get(URL, params=PARAMS)
    res = r.json()
    description = res['weather'][0]['description']
    icon = res['weather'][0]['icon']
    temp = res['main']['temp']
    day=datetime.date.today()
    return render(request, 'portfolio/api.html', {'description': description, 'icon': icon, 'temp': temp,'day': day, 'city':city})
