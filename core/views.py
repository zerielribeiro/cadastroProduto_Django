from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect

from .forms import ContatoForm, ProdutoModelForm
from .models import Produto

def index(request):
    context = {
        'produtos': Produto.objects.all()
    }
    return render(request, 'index.html', context)


def contato(request):
    form = ContatoForm(request.POST or None)
    # validando o formulario
    if str(request.method) != 'POST':
        if form.is_valid():
            form.send_mail()
            messages.success(request, 'email enviado com sucesso!')
            form = ContatoForm()
        else:
            messages.error(request,'erro ao enviar email')
    context = {
        'form': form
    }
    return render(request, 'contato.html', context)

# formulario para cadastro de produtos
def produto(request):
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == "POST":
            form = ProdutoModelForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, ' Produto cadastrado com sucesso')
                form = ProdutoModelForm()
            else:
                messages.error(request, 'Falha ao cadastrar o produto')
        else:
            form = ProdutoModelForm()
        context = {
            'form': form
        }
        return render(request, 'produto.html', context)
    else:
        return redirect('index')

