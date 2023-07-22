import re

class Persona:
    def __init__(self):
        self.nombre = ''
        self.id = ''

    def num_nomina(self):
        while True:
            self.id = input("Ingrese su número de nómina: ")
            if self.validacion(self.id, 'alphanumerico'):
                break
            else:
                self.mensaje_errores('alphanumerico')

    def nombre_usuario(self):
        while True:
            self.nombre = input("Ingrese su nombre: ")
            if self.validacion(self.nombre, 'alphabetico'):
                break
            else:
                self.mensaje_errores('alphabetico')

        
    def validacion(self, valor_entrada, tipo_entrada):
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


    def mensaje_errores(self, tipo_entrada):
        error_message = {
            'alphanumerico': "Formato incorrecto. Debe capturar solo números y letras.",
            'numerico': "Formato incorrecto. Debe capturar solo números.",
            'alphabetico': "Formato incorrecto. Debe capturar solo letras.",
            'tamanio': "Tamaño del video en formato incorrecto. Debe capturar solo números y el tamaño no debe ser mayor a 3 MB."
        }
        print(error_message[tipo_entrada])


class Video:
    def __init__(self):
        self.nombre = ''
        self.titulo = ''
        self.extension = ''
        self.tamanio = ''

    def video_nombre(self):
        while True:
            self.nombre = input("Ingrese el nombre del video: ")
            if self.validacion(self.nombre, 'alphanumerico'):
                break
            else:
                self.mensaje_errores('alphanumerico')

    def video_titulo(self):
        while True:
            self.titulo = input("Ingrese el titulo del video: ")
            if self.validacion(self.titulo, 'alphanumerico'):
                break
            else:
                self.mensaje_errores('alphanumerico')

    def video_extension(self):
        while True:
            self.extension = input("Ingrese la extensión del video: ")
            if self.validacion(self.extension, 'alphanumerico'):
                break
            else:
                self.mensaje_errores('alphanumerico')

    def video_tamanio(self):
        while True:
            self.tamanio = input("Ingrese el tamaño del video (en MB): ")
            if self.validacion(self.tamanio, 'tamanio'):
                break
            else:
                self.mensaje_errores('tamanio')

   
        
    def validacion(self, valor_entrada, tipo_entrada):
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

    def mensaje_errores(self, tipo_entrada):
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
    persona = Persona()
    persona.num_nomina()
    persona.nombre_usuario()
   
    
    videos = []
   
    num_videos = input("Ingrese la cantidad de videos a subir: ")
    print(f"\nBienvenido {persona.nombre}, tu número de nómina es {persona.id} y estás intentando subir {num_videos} videos. ¿Es correcta la información? Sí/No.")
    respuesta = input().lower()
    if respuesta == 'si':
        if not re.match("^[0-9]*$", num_videos):
                print('ingresa solo numeros')
                return False
        else:
            n_vid = int(num_videos)        
            for _ in range(n_vid):
                video = Video()
                video.video_nombre()
                video.video_titulo()
                video.video_extension()
                video.video_tamanio()
                videos.append(video)
                print("------------------------------------")
                print("¡Gracias por usar nuestro programa, Hasta la próxima! ")
                print("------------------------------------") 
                

        # Write to file
        with open('salida_avance2.txt', 'w') as f:
            f.write(f'#nomina:{persona.id} | nombre:{persona.nombre} | #videos: {num_videos}')
            for video in videos:
                f.write(f' | nombreV:{video.nombre} | tituloV:{video.titulo} | formato:{video.extension} | MB:{video.tamanio}')
        
        break
    
    elif respuesta == 'no':
            continue_option = input("¿Desea salir del sistema? Sí/No: ").lower()
            if continue_option == 'sí' or continue_option == 'si':
                print("Muchas gracias por haber usado nuestro sistema, hasta pronto.")
                break            
    

main()