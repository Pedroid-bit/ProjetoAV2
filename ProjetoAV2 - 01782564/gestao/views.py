from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Cliente, Pedido


class ClienteList(ListView):
    model = Cliente
    template_name = 'gestao/cliente_list.html'


class ClienteDetail(DetailView):
    model = Cliente
    template_name = 'gestao/cliente_detail.html'


class ClienteCreate(CreateView):
    model = Cliente
    fields = ['nome', 'email', 'telefone']
    template_name = 'gestao/cliente_form.html'
    success_url = reverse_lazy('cliente_list')


class ClienteUpdate(UpdateView):
    model = Cliente
    fields = ['nome', 'email', 'telefone']
    template_name = 'gestao/cliente_form.html'
    success_url = reverse_lazy('cliente_list')


class ClienteDelete(DeleteView):
    model = Cliente
    template_name = 'gestao/cliente_confirm_delete.html'
    success_url = reverse_lazy('cliente_list')


class PedidoList(ListView):
    model = Pedido
    template_name = 'gestao/pedido_list.html'


class PedidoDetail(DetailView):
    model = Pedido
    template_name = 'gestao/pedido_detail.html'


class PedidoCreate(CreateView):
    model = Pedido
    fields = ['cliente', 'descricao', 'valor', 'data', 'status']
    template_name = 'gestao/pedido_form.html'
    success_url = reverse_lazy('pedido_list')


class PedidoUpdate(UpdateView):
    model = Pedido
    fields = ['cliente', 'descricao', 'valor', 'data', 'status']
    template_name = 'gestao/pedido_form.html'
    success_url = reverse_lazy('pedido_list')


class PedidoDelete(DeleteView):
    model = Pedido
    template_name = 'gestao/pedido_confirm_delete.html'
    success_url = reverse_lazy('pedido_list')
