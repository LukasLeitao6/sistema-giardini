from django.contrib import admin
from django.core.mail import send_mail
from .models import Reserva

# --- 📋 LISTA VIP DE GESTORES (Giardini Café) ---
LISTA_EMAILS_GESTORES = [
    'lukasleitao6@gmail.com',
    'marcelopeixotobra@gmail.com',
    'giardincafe@gmail.com',
]

# Números formatados para automação (apenas dígitos, com código do país 55)
LISTA_WHATSAPP_GESTORES = [
    '5585991794422',
    '5585998099513',
    '5585991371491',
]

def enviar_whatsapp_simulado(numero, mensagem):
    # Simulação do envio. Futuramente aqui entra a conexão com a API.
    print(f"\n📲 [WHATSAPP PARA {numero}]:\n{mensagem}\n")

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('nome_cliente', 'data_evento', 'status', 'numero_pessoas', 'telefone_whatsapp')
    list_filter = ('status', 'data_evento')
    search_fields = ('nome_cliente', 'telefone_whatsapp', 'email_cliente')
    
    # Organização visual
    fieldsets = (
        ('Dados do Cliente', {
            'fields': ('nome_cliente', 'data_evento', 'tipo_evento', 'numero_pessoas', 'telefone_whatsapp', 'email_cliente')
        }),
        ('Área do Gestor (Confirmação)', {
            'fields': ('status', 'valor_acertado', 'local_giardini', 'tema_decoracao', 'coffee_break'),
        }),
    )

    # --- O CÉREBRO DA OPERAÇÃO ---
    def save_model(self, request, obj, form, change):
        # Verifica se é uma edição (change) E se o status mudou para 'CONFIRMADO'
        if change and 'status' in form.changed_data and obj.status == 'CONFIRMADO':
            
            # 1. Monta a mensagem formatada
            mensagem_formatada = (
                f"🚨 *GIARDINI: NOVA RESERVA FECHADA!* 🚨\n\n"
                f"👤 *Cliente:* {obj.nome_cliente}\n"
                f"📅 *Data:* {obj.data_evento.strftime('%d/%m/%Y às %H:%M')}\n"
                f"👥 *Pessoas:* {obj.numero_pessoas}\n"
                f"📍 *Local:* {obj.local_giardini}\n"
                f"💰 *Valor:* R$ {obj.valor_acertado}\n"
                f"📝 *Tema:* {obj.tema_decoracao}\n"
                f"☕ *Coffee:* {obj.coffee_break}\n"
            )

            # 2. Loop para enviar aos 3 E-mails
            print(f"--- Disparando e-mails para a diretoria... ---")
            send_mail(
                subject=f'✅ Reserva Confirmada: {obj.nome_cliente}',
                message=mensagem_formatada,
                from_email='sistema@giardinicafe.com.br',
                recipient_list=LISTA_EMAILS_GESTORES,
                fail_silently=False,
            )

            # 3. Loop para enviar aos 3 WhatsApps
            print(f"--- Disparando WhatsApps para a diretoria... ---")
            for numero in LISTA_WHATSAPP_GESTORES:
                enviar_whatsapp_simulado(numero, mensagem_formatada)

        super().save_model(request, obj, form, change)
        