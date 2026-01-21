from django import forms
from .models import Reserva

class FormularioReserva(forms.ModelForm):
    class Meta:
        model = Reserva
        # Aqui definimos SÓ o que o cliente pode preencher
        fields = ['nome_cliente', 'data_evento', 'tipo_evento', 'numero_pessoas', 'telefone_whatsapp', 'email_cliente']
        
        # Isso aqui é para deixar o campo de data mais bonito (com calendário)
        widgets = {
            'data_evento': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'nome_cliente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu nome completo'}),
            'tipo_evento': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Aniversário, Confraternização'}),
            'numero_pessoas': forms.NumberInput(attrs={'class': 'form-control'}),
            'telefone_whatsapp': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(85) 99999-9999'}),
            'email_cliente': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'seu@email.com'}),
        }