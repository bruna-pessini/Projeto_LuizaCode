from django.shortcuts import render, redirect, HttpResponse
from app.forms import ProdutosForm
from app.models import Produto, Empresa
import json

def home(request, pk):
    data = {}
    data['db'] = Produto.objects.filter(empresa_id=pk)
    return render(request, 'indexProducts.html', data)

def form(request, pk):
    data = {}
    data['form'] = ProdutosForm()
    data["empresa_id"] = pk
    return render(request, 'productsForm.html', data)

def create(request, pk):
    empresa = Empresa.objects.get(pk=pk)
    produto = Produto(empresa=empresa, nome=request.POST.get('nome'),
                      codigo=request.POST.get('codigo'),
                      descricao=request.POST.get('descricao'),
                      marca=request.POST.get('marca'),
                      valor=request.POST.get('valor')
                      )
    produto.save()
    return redirect('homeproduto', pk)

def view(request, pk):
    data = {}
    data['db'] = Produto.objects.get(pk=pk)
    return render(request, 'viewProducts.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Produto.objects.get(pk=pk)
    data['form'] = ProdutosForm(instance=data['db'])
    return render(request, 'productsForm.html', data)

def update(request, pk):
    data = {}
    data['db'] = Produto.objects.get(pk=pk)
    form = ProdutosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(request, pk):
    db = Produto.objects.get(pk=pk)
    db.delete()
    return redirect('home')

