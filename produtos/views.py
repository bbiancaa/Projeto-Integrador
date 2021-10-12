from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic.edit import FormMixin, FormView
from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Produto
from .forms import ProdutoForm


class CreateProductView(CreateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'produtos/form_produto.html'


class ListProductView(ListView):
    model = Produto
    paginate_by = 5
    ordering = 'cod_produto'
    template_name = 'produtos/list_products.html'

    def get_queryset(self):
        nome_produto = self.request.GET.get('q_produto', '')
        object_list = self.model.objects.all().order_by('cod_produto')
        print(nome_produto)
        if nome_produto:
            object_list = object_list.filter(nome_produto__icontains=nome_produto)
        return object_list


class DetailProductView(DetailView, FormMixin):
    model = Produto
    template_name = 'produtos/detail_products.html'
    form_class = ProdutoForm

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.id})


class UpdateProductView(UpdateView):
    model = Produto
    template_name = 'produtos/detail_products.html'
    form_class = ProdutoForm
