from django.shortcuts import render, redirect
from .models import Pessoa
from .forms import PessoaForm
from django.shortcuts import get_object_or_404
def cadastrar(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastrar')
    else:
        form = PessoaForm()

    pessoas = Pessoa.objects.all()
    return render(request, 'cadastro/cadastrar.html', {
        'form': form,
        'pessoas': pessoas
    })

def excluir_pessoa(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)
    pessoa.delete()
    return redirect('cadastrar')
