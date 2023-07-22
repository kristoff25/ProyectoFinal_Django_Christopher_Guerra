from django.shortcuts import render, redirect
from .forms import UsuarioVideoForm
from .models import TBL_Usuario, TBL_Video, TBL_Usuario_Video  
def inicio(request):
    return render(request, 'paginas/inicio.html')

def formulario(request):
    if request.method == 'POST':
        form = UsuarioVideoForm(request.POST)
        if form.is_valid():
            usuario = TBL_Usuario(
                id=form.cleaned_data['usuario_id'],
                nombre=form.cleaned_data['usuario_nombre']
            )
            usuario.save()

            video = TBL_Video(
                nombre=form.cleaned_data['video_nombre'],
                extension=form.cleaned_data['video_extension'],
                tamaño=form.cleaned_data['video_tamaño']
            )
            video.save()

            usuario_video = TBL_Usuario_Video(
                id_usuario=usuario,
                id_video=video
            )
            usuario_video.save()

            return redirect('inicio') 
    else:
        form = UsuarioVideoForm()

    return render(request, 'paginas/formulario.html', {'form': form})

