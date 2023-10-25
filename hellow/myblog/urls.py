
from django.urls import path
from . import views
urlpatterns = [
    path('blog/', views.myblogsite),
    path('', views.blogpessoal, name='blogpessoal'),
    path('contato/', views.formsview, name='formsview'),
    path('processa_forms/', views.processadorforms, name='processa_forms'),
    path('listar_usuario/', views.listarforms, name='listar_usuario'),
    path('Update_usuario/<int:id>', views.Update_usuario, name='update_usuario'),
    path('delete_usuario/<int:id>', views.delete_usuario, name='delete_usuario')
    
]
