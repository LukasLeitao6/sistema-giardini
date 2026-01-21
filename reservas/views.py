from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail # <--- PRECISA DESSA IMPORTAÇÃO
from .forms import FormularioReserva

def criar_reserva(request):
    if request.method == 'POST':
        form = FormularioReserva(request.POST)
        if form.is_valid():
            reserva = form.save() # Salvamos a reserva numa variável para pegar os dados dela
            
            # --- DISPARO DE E-MAIL (NOVA SOLICITAÇÃO) ---
            print("--- Enviando e-mail de aviso ---")
            send_mail(
                subject=f'Nova Reserva: {reserva.nome_cliente}',
                message=f'O cliente {reserva.nome_cliente} pediu uma reserva para {reserva.data_evento}. \nEntre no painel para confirmar.',
                from_email='sistema@giardinicafe.com.br',
                recipient_list=['reservas@giardinicafe.com.br'], # E-mail do seu setor de reservas
                fail_silently=False,
            )
            
            messages.success(request, 'Sua solicitação foi enviada! Nossa equipe entrará em contato.')
            return redirect('home')
    else:
        form = FormularioReserva()

    return render(request, 'reservas/formulario.html', {'form': form})