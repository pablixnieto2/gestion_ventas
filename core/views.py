from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Cliente, Producto, Venta, VentaProducto, Pago
from django.shortcuts import render
from .forms import ClienteForm, ProductoForm, VentaForm, PagoForm, VentaProductoFormSet

def home(request):
    return render(request, 'core/home.html')

class ClienteListView(ListView):
    model = Cliente
    template_name = 'core/listar_clientes.html'
    context_object_name = 'clientes'

class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'core/detalle_cliente.html'

class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'core/crear_cliente.html'
    success_url = reverse_lazy('cliente-list')

    def form_valid(self, form):
        cliente = form.save(commit=False)
        cliente.id_cliente = f"CL{timezone.now().strftime('%Y%m%d%H%M%S')}"
        cliente.created_by = self.request.user.email
        cliente.vendedora = self.request.user.username
        cliente.save()
        return super().form_valid(form)

class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'core/editar_cliente.html'
    success_url = reverse_lazy('cliente-list')

class ClienteDeleteView(UpdateView):
    model = Cliente
    template_name = 'core/eliminar_cliente.html'
    success_url = reverse_lazy('cliente-list')
    fields = []

    def post(self, request, *args, **kwargs):
        cliente = self.get_object()
        cliente.estado = 'eliminar cliente duplicado'
        cliente.save()
        return redirect(self.success_url)

class ProductoListView(ListView):
    model = Producto
    template_name = 'core/listar_productos.html'
    context_object_name = 'productos'

class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'core/detalle_producto.html'

class ProductoCreateView(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'core/crear_producto.html'
    success_url = reverse_lazy('producto-list')

    def form_valid(self, form):
        producto = form.save(commit=False)
        producto.id_producto = f"PR{timezone.now().strftime('%Y%m%d%H%M%S')}"
        producto.save()
        return super().form_valid(form)

class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'core/editar_producto.html'
    success_url = reverse_lazy('producto-list')

class ProductoDeleteView(UpdateView):
    model = Producto
    template_name = 'core/eliminar_producto.html'
    success_url = reverse_lazy('producto-list')
    fields = []

    def post(self, request, *args, **kwargs):
        producto = self.get_object()
        producto.estado = 'Eliminado'
        producto.save()
        return redirect(self.success_url)

class VentaListView(ListView):
    model = Venta
    template_name = 'core/listar_ventas.html'
    context_object_name = 'ventas'

class VentaDetailView(DetailView):
    model = Venta
    template_name = 'core/detalle_venta.html'

class VentaCreateView(CreateView):
    model = Venta
    form_class = VentaForm
    template_name = 'core/crear_venta.html'
    success_url = reverse_lazy('venta-list')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['formset'] = VentaProductoFormSet(self.request.POST)
        else:
            data['formset'] = VentaProductoFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if form.is_valid() and formset.is_valid():
            venta = form.save(commit=False)
            venta.id_venta = f"VT{timezone.now().strftime('%Y%m%d%H%M%S')}"
            venta.created_by = self.request.user.email
            venta.estado_entrega = "Por Entregar o Enviar"
            venta.save()
            formset.instance = venta
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))


class VentaUpdateView(UpdateView):
    model = Venta
    form_class = VentaForm
    template_name = 'core/editar_venta.html'
    success_url = reverse_lazy('venta-list')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['formset'] = VentaProductoFormSet(self.request.POST, instance=self.object)
        else:
            data['formset'] = VentaProductoFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))


class VentaDeleteView(UpdateView):
    model = Venta
    template_name = 'core/eliminar_venta.html'
    success_url = reverse_lazy('venta-list')
    fields = []

    def post(self, request, *args, **kwargs):
        venta = self.get_object()
        venta.estado_entrega = 'Eliminado'
        venta.save()
        return redirect(self.success_url)

class PagoListView(ListView):
    model = Pago
    template_name = 'core/listar_pagos.html'
    context_object_name = 'pagos'

class PagoDetailView(DetailView):
    model = Pago
    template_name = 'core/detalle_pago.html'

class PagoCreateView(CreateView):
    model = Pago
    form_class = PagoForm
    template_name = 'core/crear_pago.html'
    success_url = reverse_lazy('pago-list')

    def form_valid(self, form):
        pago = form.save(commit=False)
        pago.id_pago = f"PA{timezone.now().strftime('%Y%m%d%H%M%S')}"
        pago.created_by = self.request.user.email
        pago.save()
        return super().form_valid(form)

class PagoUpdateView(UpdateView):
    model = Pago
    form_class = PagoForm
    template_name = 'core/editar_pago.html'
    success_url = reverse_lazy('pago-list')

class PagoDeleteView(UpdateView):
    model = Pago
    template_name = 'core/eliminar_pago.html'
    success_url = reverse_lazy('pago-list')
    fields = []

    def post(self, request, *args, **kwargs):
        pago = self.get_object()
        pago.estado = 'Eliminado'
        pago.save()
        return redirect(self.success_url)