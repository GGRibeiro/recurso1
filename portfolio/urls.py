from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = 'portfolio'




urlpatterns = [
    path('base/', views.base_view, name='base'),
    path('', views.home_view, name='home'),
    path('contacto/', views.contacto_view, name='contacto'),
    path('projetos/', views.projetos_view, name='projetos'),
    path('sobre/', views.render_semestre_view, name='sobre'),
    path('blog/', views.home_page_view, name='blog'),

    path('criaArtigo/', views.criaArtigo, name='criaArtigo'),
    path('editaArtigo/<int:tarefa_id>/', views.edita_Artigo_View, name='editaArtigo'),
    path('apagaArtigo/<int:tarefa_id>/', views.apaga_Artigo_View, name='apagaArtigo'),

    path('novoComentario/', views.novoComentario_View, name='novoComentario'),
    path('apagaComentario/<int:comentario_id>/', views.apagaComentario_View, name='apagaComentario'),

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('user/', views.user_view, name='user'),


    path('sobre/cadastraSemestre.html', views.cadastraSemestre, name='cadastraSemestre'),
    path('api/', views.indexApi_View, name="indexApi"),










]
