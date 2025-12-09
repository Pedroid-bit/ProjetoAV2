from django.urls import path
from . import views

urlpatterns = [
    # Clientes
    path('', views.ClienteList.as_view(), name='cliente_list'),
    path('clientes/<int:pk>/', views.ClienteDetail.as_view(), name='cliente_detail'),
    path('clientes/add/', views.ClienteCreate.as_view(), name='cliente_add'),
    path('clientes/<int:pk>/edit/', views.ClienteUpdate.as_view(), name='cliente_edit'),
    path('clientes/<int:pk>/delete/', views.ClienteDelete.as_view(), name='cliente_delete'),

    # Pedidos
    path('pedidos/', views.PedidoList.as_view(), name='pedido_list'),
    path('pedidos/<int:pk>/', views.PedidoDetail.as_view(), name='pedido_detail'),
    path('pedidos/add/', views.PedidoCreate.as_view(), name='pedido_add'),
    path('pedidos/<int:pk>/edit/', views.PedidoUpdate.as_view(), name='pedido_edit'),
    path('pedidos/<int:pk>/delete/', views.PedidoDelete.as_view(), name='pedido_delete'),
]
