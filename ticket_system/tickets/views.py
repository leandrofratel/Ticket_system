from django.shortcuts import render, get_object_or_404, redirect
from .forms import TicketForm, TicketImageForm
from .models import Ticket, TicketImage

def ticket_list(request):
    tickets = Ticket.objects.all()
    return render(request, 'tickets/ticket_list.html', {'tickets': tickets})

def ticket_create(request):
    if request.method == 'POST':
        ticket_form = TicketForm(request.POST)
        if ticket_form.is_valid():
            ticket = ticket_form.save()

            # Processa as imagens
            for file in request.Files.getlist('image'):
                TicketImage.objects.create(ticket=ticket, image=file)
            return redirect('ticket_list')
    else:
        ticket_form = TicketForm()
    return render(request, 'tickets/ticket_form.html', {'ticket_form': ticket_form})

def ticket_update(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    if request.method == 'POST':
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('ticket_list')
    else:
        form = TicketForm(instance=ticket)
    return render(request, 'tickets/ticket_form.html', {'form': form})

def ticket_delete(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    if request.method == 'POST':
        ticket.delete()
        return redirect('ticket_list')
    return render(request, 'tickets/ticket_confirm_delete.html', {'ticket': ticket})

def ticket_detail(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    return render(request, 'tickets/ticket_detail.html', {'ticket':ticket})