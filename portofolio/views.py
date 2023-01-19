from django.shortcuts import render
from django.contrib import messages
from perfil.models import Perfil,RedesSociales,Proyectos,Descripcion,Habilidades,Formacion,Experiencia
from django.contrib.auth.models import User
from portofolio.forms import ContactoForm

# Create your views here.

def ver_portofolio(request,user):


    data_proyecto= User.objects.all().get(username=user)
    id_user = data_proyecto.id

    #Necesitamos traernos toda la info de todas las uniones
    perfil = Perfil.objects.all().get(user_id=id_user)
    redessociales = RedesSociales.objects.all().get(user_id=id_user)
    habilidades = Habilidades.objects.filter(user_id=id_user)
    formacion = Formacion.objects.all().get(user_id=id_user)
    experiencia = Experiencia.objects.filter(user_id=id_user)

    proyectos = Proyectos.objects.filter(user_id=id_user)
    descripcion = Descripcion.objects.all().get(user_id=id_user)
    form_contacto = ContactoForm();
    #print('Habilidades -> ',habilidades[1])

    context={
        'perfil':perfil,
        'redessociales':redessociales,
        'habilidades':habilidades,
        'formacion':formacion,
        'experiencias':experiencia,
        'proyectos':proyectos,
        'username':user,
        'descripcion':descripcion,
        'form_contacto':form_contacto,
        'id_user':id_user,
    }


    #context = {'username':username}
    return render(request,'usuario/portofolio.html',context)
    

def contacto(request):
    if request.method=='POST':
        form=ContactoForm(request.POST)
        #print('id_user-> ',user_id)
        #form.save()
        if form.is_valid():
            form.save()
            #messages.success(request,f'Mensjae enviado!')
            #return redirect('ver-portofolio')
        else:
            #messages.success(request,f'Formulario incorrecto')
            #form=ContactoForm()
            print('')
            
        context={
            'ok':200
        }
        return render(request,'usuario/ok.html',context)



