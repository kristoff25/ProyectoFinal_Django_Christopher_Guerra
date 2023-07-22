import re

# Una función para mostrar los mensajes de error de validación
def mensaje_errores(tipo_entrada):
    error_message = {
        'alphanumerico': "Formato incorrecto. Debe capturar solo números y letras.",
        'numerico': "Formato incorrecto. Debe capturar solo números.",
        'alphabetico': "Formato incorrecto. Debe capturar solo letras.",
        'tamanio': "Tamaño del video en formato incorrecto. Debe capturar solo números y el tamaño no debe ser mayor a 3 MB."
    }
    print(error_message[tipo_entrada])


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

#  información del usuario
def info_usuario():
    while True:
        num_nomina = input("Ingrese su número de nómina: ")
        if validacion(num_nomina, 'alphanumerico'):
            break
        else:
            mensaje_errores('alphanumerico')

    while True:
        nombre = input("Ingrese su nombre: ")
        if validacion(nombre, 'alphabetico'):
            break
        else:
            mensaje_errores('alphabetico')

    while True:
        num_videos = input("Ingrese la cantidad de videos a subir: ")
        if validacion(num_videos, 'numerico'):
            break
        else:
            mensaje_errores('numerico')

    return num_nomina, nombre, int(num_videos)

def usuarios_videos(num_videos):
    videos = []
    
    for i in range(num_videos):
        print(f"\nRecopilando información para el video {i + 1}:")

        while True:
            video_titulo = input("Ingrese el título del video: ")
            if validacion(video_titulo, 'alphanumeric'):
                break
            else:
                mensaje_errores('alphanumerico')

        while True:
            video_nombre = input("Ingrese el nombre del video: ")
            if validacion(video_nombre, 'alphanumerico'):
                break
            else:
                mensaje_errores('alphanumerico')

        while True:
            video_extension = input("Ingrese la extensión del video: ")
            if validacion(video_extension, 'alphanumerico'):
                break
            else:
                mensaje_errores('alphanumerico')

        while True:
            video_size = input("Ingrese el tamaño del video (en MB): ")
            if validacion(video_size, 'tamanio'):
                break
            else:
                mensaje_errores('tamanio')

        videos.append((video_titulo, video_nombre, video_extension, video_size))

    print(videos)

    return videos 

def salida(num_nomina, nombre, num_videos, videos):
    with open('salida_avance1.txt', 'w') as f:
        f.write(f'#nomina:{num_nomina} | nombre:{nombre} | #videos:{num_videos}')
        for video in videos:
            f.write(f' | nombreV:{video[0]} | tituloV:{video[1]} | formato:{video[2]} | MB:{video[3]}')

          
def iniciarApp():
    while True:
        print("------------------------------------")
        print("Bienvenido al sistema ingrese los siguientes datos: ")
        print("------------------------------------")
        num_nomina, nombre, num_videos = info_usuario() 
        print(f"\nBienvenido {nombre}, tu número de nómina es {num_nomina} y estás intentando subir {num_videos} videos. ¿Es correcta la información? Sí/No.")
        respuesta = input().lower()
        if respuesta == 'si':
            videos = usuarios_videos(num_videos)
            salida(num_nomina, nombre, num_videos, videos)
            print("------------------------------------")
            print("¡Gracias por usar nuestro programa, Hasta la próxima! ")
            print("------------------------------------")
            break
        elif respuesta == 'no':
            continue_option = input("¿Desea salir del sistema? Sí/No: ").lower()
            if continue_option == 'sí' or continue_option == 'si':
                print("Muchas gracias por haber usado nuestro sistema, hasta pronto.")
                break


iniciarApp()
