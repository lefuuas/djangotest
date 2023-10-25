from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import usuario
from .forms import Usuariosapp

def myblogsite(request):
    return HttpResponse("hellow world")

def blogpessoal(request):
    return render(request, 'blogpessoal/blog.html')

def formsview(request):
    return render(request, 'blogpessoal/contato.html')

def processadorforms(reqeust):
    form = Usuariosapp(reqeust.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_usuario')
    return render(reqeust , 'blogpessoal/contato.html', {'form': form })

def listarforms(request):
    usuarios = usuario.objects.all()
    return render(request, 'blogpessoal/usuarios.html', {'usuarios': usuarios})

def Update_usuario(request, id):
    usuarioatt = usuario.objects.get(id = id)
    form = Usuariosapp(request.POST or None, instance= usuarioatt)
    if form.is_valid():
        form.save()
        return redirect('listar_usuario')
    return render(request , 'blogpessoal/contato.html', {'form': form, 'usuarioatt': usuarioatt})

def delete_usuario(request, id):
    usuaarios = usuario.objects.get(id =id)
    if request.method == 'GET':
        usuaarios.delete()
        return redirect('listar_usuario')
    return render(request , 'blogpessoal/blog.html')

