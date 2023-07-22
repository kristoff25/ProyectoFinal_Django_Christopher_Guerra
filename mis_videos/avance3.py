import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mis_videos.settings")
django.setup()

from avance3.models import TBL_Usuario, TBL_Video, TBL_Usuario_Video
import re

def num_nomina():
    while True:
        id = input("Ingrese su número de nómina: ")
        if validacion(id, 'alphanumerico'):
            return id
        else:
            mensaje_errores('alphanumerico')

def nombre_usuario():
    while True:
        nombre = input("Ingrese su nombre: ")
        if validacion(nombre, 'alphabetico'):
            return nombre
        else:
            mensaje_errores('alphabetico')

def video_nombre():
    while True:
        nombre = input("Ingrese el nombre del video: ")
        if validacion(nombre, 'alphanumerico'):
            return nombre
        else:
            mensaje_errores('alphanumerico')

def video_extension():
    while True:
        extension = input("Ingrese la extensión del video: ")
        if validacion(extension, 'alphanumerico'):
            return extension
        else:
            mensaje_errores('alphanumerico')

def video_tamanio():
    while True:
        tamanio = input("Ingrese el tamaño del video (en MB): ")
        if validacion(tamanio, 'tamanio'):
            return int(tamanio)
        else:
            mensaje_errores('tamanio')

def validacion(valor_entrada, tipo_entrada):
    if tipo_entrada == 'alphabetico':
        if not re.match("^[A-Za-z]*$", valor_entrada):
            return False
    elif tipo_entrada == 'alphanumerico':
        if not re.match("^[A-Za-z0-9]*$", valor_entrada):
            return False
    elif tipo_entrada == 'tamanio':
        if not re.match("^[0-9]*$", valor_entrada) or not(0 <= int(valor_entrada) <= 3):
            return False
    return True

def mensaje_errores(tipo_entrada):
    error_message = {
        'alphanumerico': "Formato incorrecto. Debe capturar solo números y letras.",
        'numerico': "Formato incorrecto. Debe capturar solo números.",
        'alphabetico': "Formato incorrecto. Debe capturar solo letras.",
        'tamanio': "Tamaño del video en formato incorrecto. Debe capturar solo números y el tamaño no debe ser mayor a 3 MB."
    }
    print(error_message[tipo_entrada])

def main():
 while True:
    print("------------------------------------")
    print("Bienvenido al sistema ingrese los siguientes datos: ")
    print("------------------------------------")
    id = num_nomina()
    nombre = nombre_usuario()
    usuario = TBL_Usuario(id=id, nombre=nombre)
    usuario.save()

    num_videos = input("Ingrese la cantidad de videos a subir: ")
    n_vid = int(num_videos)        
    for _ in range(n_vid):
        nombre = video_nombre()
        extension = video_extension()
        tamanio = video_tamanio()
        video = TBL_Video(nombre=nombre, extension=extension, tamaño=tamanio)
        video.save()
        usuario_video = TBL_Usuario_Video(id_usuario=usuario, id_video=video)
        usuario_video.save()

    print("------------------------------------")
    print("¡Gracias por usar nuestro programa, Hasta la próxima! ")
    print("------------------------------------") 
    break

main()
