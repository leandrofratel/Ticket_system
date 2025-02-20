from django.db import models

class Ticket(models.Model):
    STATUS_CHOICES = [
        ('Aberto', 'Aberto'),
        ('Fechado', 'Fechado'),
        ('Resolvido', 'Resolvido'),
        ('Em Andamento', 'Em Andamento'),
        ('Designado', 'Designado'),
        ('Em Análise', 'Em Análise'),
        ('Sala de Crise', 'Sala de Crise'),
    ]

    SUPORTE_CHOICES = [
        ('grupo_operacoes_integradas','COI - Grupo de Operações Integradas'),
        ('operacoes_ibm','Operações IBM'),
    ]

    ANALISTAS_CHOICES = [
        ('Leandro Fratel','Leandro Fratel'),
        ('Heráclito Teixeira','Heráclito Teixeira'),
        ('Camilla Gama','Camilla Gama'),
    ]

    codigo_incidente = models.CharField(max_length=50, verbose_name="Incidente")
    codigo_sx = models.CharField(max_length=50, verbose_name="SX")
    
    recurso = models.CharField(max_length=50, verbose_name="Recurso")
    responsavel = models.CharField(max_length=50, verbose_name="Responsável")
    problema_apresentado = models.TextField(verbose_name="Problema Apresentado")
    acoes = models.TextField(verbose_name="Ações")
    solucao = models.TextField(verbose_name="Solução")
    causa_raiz = models.TextField(verbose_name="Causa Raiz")
    link_alerta = models.URLField(verbose_name="Link do Alerta", blank=True, null=True)
    
    grupo_suporte = models.CharField(max_length=100, choices=SUPORTE_CHOICES, default='', verbose_name="Grupo de Suporte")
    analista = models.CharField(max_length=100, choices=ANALISTAS_CHOICES, default='', verbose_name="Analista")
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Aberto', verbose_name="Status")
    
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    atualizado_em = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    def __str__(self):
        return self.codigo_incidente, self.responsavel
    
class TicketImage(models.Model):
    ticket = models.ForeignKey(Ticket, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='tickets/images/')

    def __str__(self):
        return f"Imagem do Ticket {self.ticket.codigo_incidente}"
