from django import forms
from .models import Solicitud

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = '__all__'
        widgets = {
            'nombre_solicitante': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre completo'}),
            'documento_identidad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Documento de identidad'}),
            'correo_electronico': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'correo@ejemplo.com'}),
            'telefono_contacto': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}),
            'tipo_solicitud': forms.Select(attrs={'class': 'form-control'}),
            'asunto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Asunto de la solicitud'}),
            'descripcion_detallada': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'fecha_solicitud': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'archivo_adjunto': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
