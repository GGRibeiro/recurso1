from django import forms
from django.forms import ModelForm

from .models import Tarefa, Comentario
from .models import Semestre


class TarefaForm(ModelForm):
        class  Meta:
            model = Tarefa
            fields = '__all__'


class SemestreForm(ModelForm):
    class Meta:
        model = Semestre
        fields = '__all__'



class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario
        fields = '__all__'
