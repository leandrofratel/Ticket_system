from django.shortcuts import render, get_object_or_404, redirect
from .forms import TicketForm
from .models import Ticket, TicketImage

def ticket_list(request):
    """ Lista todos os tickets cadastrados no sistema. """
    tickets = Ticket.objects.all()
    return render(request, 'tickets/ticket_list.html', {'tickets': tickets})

def ticket_create(request):
    """
    Cria um novo ticket.
    - Se a requisição for POST, valida e salva o ticket, além de processar o upload de imagens.
    - Se a requisição for GET, exibe o formulário vazio para criação de um novo ticket.
    """
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save()
            for file in request.FILES.getlist('images'):
                TicketImage.objects.create(ticket=ticket, image=file)
            return redirect('ticket_list')
    else:
        form = TicketForm()
    return render(request, 'tickets/ticket_form.html', {'form': form})

def ticket_update(request, pk):
    """
    Atualiza um ticket existente.
    - Se a requisição for POST, valida e atualiza o ticket, além de processar o upload de novas imagens.
    - Se a requisição for GET, exibe o formulário preenchido com os dados do ticket para edição.
    """
    ticket = get_object_or_404(Ticket, pk=pk)
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            ticket = form.save()
            for file in request.FILES.getlist('images'):
                TicketImage.objects.create(ticket=ticket, image=file)
            return redirect('ticket_list')
    else:
        form = TicketForm(instance=ticket)
    return render(request, 'tickets/ticket_form.html', {'form': form})

def ticket_delete(request, pk):
    """
    Exclui um ticket existente.
    - Se a requisição for POST, exclui o ticket do banco de dados.
    - Se a requisição for GET, exibe uma página de confirmação para exclusão do ticket.
    """
    ticket = get_object_or_404(Ticket, pk=pk)
    if request.method == 'POST':
        ticket.delete()
        return redirect('ticket_list')
    return render(request, 'tickets/ticket_confirm_delete.html', {'ticket': ticket})

def ticket_detail(request, pk):
    """
    Exibe os detalhes de um ticket específico.
    - Recupera um ticket com base no pk (chave primária) e exibe suas informações.
    """
    ticket = get_object_or_404(Ticket, pk=pk)
    return render(request, 'tickets/ticket_detail.html', {'ticket': ticket})