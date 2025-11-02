from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import views
from Linkedin.models import projetosModel 
from Linkedin.forms import projetosForm 
from Linkedin.forms import contatoForm
from django.core.mail import send_mail



def contato(request):
    contexto = {
        "form": contatoForm()
    }
    if request.method == 'POST':
        form = contatoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data ['nome']
            numero = form.cleaned_data ['numero']
            email = form.cleaned_data ['email']
            mensagem = form.cleaned_data.get('mensagem', '')

            mensagem = f"""
            novo envio pelo formulario:
            nome: {nome}
            numero: {numero}
            email: {email}
            mensagem: {mensagem}
            """
            send_mail(
            'novo envio do fromulario',
            mensagem,
            'vitorrianpdaluz@gmail.com',
            ['vitorrianpdaluz@gmail.com'],
            fail_silently= False,
            )
            
            return render(request, 'LinkedinHome/home.html')
        else:
            form = contatoForm()

    return render(request, 'LinkedinContato/contato.html', contexto)

def projeto(request):
    # Busca todos os projetos
    projetos = projetosModel.objects.all()
    for p in projetos:
        p.tecnologias_lista = p.tecnologia.split(',') if p.tecnologia else []

    form = projetosForm()

    if request.method == 'POST':
        form = projetosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    # Renderiza o template
    return render(request, 'LinkedinPortifolio/portifolio.html', {'projetos': projetos, 'form': form})
