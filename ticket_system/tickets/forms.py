from django import forms
from .models import Ticket, TicketImage

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
            'codigo_incidente', 'codigo_sx', 'recurso', 
            'responsavel', 'problema_apresentado','acoes',
            'solucao', 'causa_raiz', 'link_alerta',
            'grupo_suporte', 'analista', 'status'
        ]
        widgets = {
            'problema_apresentado': forms.Textarea(attrs={'rows': 3}),
            'acoes': forms.Textarea(attrs={'rows': 3}),
            'solucao': forms.Textarea(attrs={'rows': 3}),
            'causa_raiz': forms.Textarea(attrs={'rows': 3}),
        }

class TicketImageForm(forms.ModelForm):
    class Meta:
        model = TicketImage
        fields = ['image']