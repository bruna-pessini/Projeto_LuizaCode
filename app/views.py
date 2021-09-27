from django.shortcuts import render, redirect, HttpResponse
from app.forms import EmpresaForm
from app.models import Empresa, Produto
from django.core import serializers


def home(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Empresa.objects.filter(nome__icontains=search)
    else:
        data['db'] = Empresa.objects.all()
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = EmpresaForm()
    return render(request, 'form.html', data)

def create(request):
    form = EmpresaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('home')


def view(request, pk):
    data = {}
    data['db'] = Empresa.objects.get(pk=pk)
    return render(request, 'view.html', data)


def edit(request, pk):
    data = {}
    data['db'] = Empresa.objects.get(pk=pk)
    data['form'] = EmpresaForm(instance=data['db'])
    return render(request, 'form.html', data)


def update(request, pk):
    data = {}
    data['db'] = Empresa.objects.get(pk=pk)
    form = EmpresaForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')


def delete(request, pk):
    db = Empresa.objects.get(pk=pk)
    db.delete()
    return redirect('home')


def produtos(request, pk):
    data = {}
    data['db'] = Produto.objects.filter(empresa_id=pk)
    data["empresa_id"] = pk
    print(data)
    return render(request, "indexProducts.html", data)



