from django.urls import path
from . import views

urlpatterns = [
    path('', views.cadastrar, name='cadastrar'),
    path('excluir/<int:id>/', views.excluir_pessoa, name='excluir_pessoa'),
]
