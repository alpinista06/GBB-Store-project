from django.urls import path

from . import views

urlpatterns = [
    path("hello/", views.HelloThereView.as_view(), name="hello-there-view"),
    path("dashboard/ferramenta/criar/", views.CriarFerramentaView.as_view(), name="criar-ferramenta-view"),
    path("dashboard/accounts/credito/criar/", views.InserirCreditoView.as_view(), name="inserir-credito-view"),
    path("dashboard/accounts/credito/criar/solicitacoes/", views.GetImportTools, name="inserir-solicitacoes-view"),
]
