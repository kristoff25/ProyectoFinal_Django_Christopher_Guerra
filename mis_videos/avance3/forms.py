from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import TBL_Usuario, TBL_Video


class UserForm(forms.ModelForm):
    class Meta:
        model = TBL_Usuario
        fields = ['id', 'nombre']

class VideosForm(forms.ModelForm):
    class Meta:
        model = TBL_Video
        fields = ['nombre', 'extension', 'tamaño']

class UsuarioVideoForm(forms.Form):
    usuario_id = forms.CharField(max_length=10, label='ID de Usuario')
    usuario_nombre = forms.CharField(max_length=50, label='Nombre de Usuario')
    video_nombre = forms.CharField(max_length=50, label='Nombre del Video')
    video_extension = forms.CharField(max_length=5, label='Extension del Video(mp4, mov...)')
    video_tamaño = forms.IntegerField(
        label='Tamaño del Video MB Max 3MB:', 
        validators=[
            MinValueValidator(1, message='El tamaño debe ser al menos 1'),
            MaxValueValidator(3, message='Error al subir los videos El tamaño del video no puede ser más de 3MB')
        ]
    )