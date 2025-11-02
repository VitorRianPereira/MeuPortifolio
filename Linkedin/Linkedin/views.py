from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.http import HttpRequest
from .forms import projetosForm
from .models import projetosModel

def portifolio(request):
    return render(request, 'LinkedinPortifolio/portifolio.html')

def sobre(request):
    return render(request, 'LinkedinSobreMim/sobremim.html')

def index_view(request):
    conntexto = {
        "projetos":projetosModel.objects.all()
    }
    return render(request, 'LinkedinHome/home.html')

def administracao(request: HttpRequest):
    if request.method == "POST":
        formulario = projetosForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("home")
    contexto = {
        "form":projetosForm()
    }
    return render(request, 'LinkedinAdmin/admin.html', contexto)
   