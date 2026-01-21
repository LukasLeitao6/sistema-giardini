from django.db import models

class Reserva(models.Model):
    # Opções de Status para o Gestor controlar
    STATUS_CHOICES = [
        ('PENDENTE', 'Aguardando Análise'),
        ('CONFIRMADO', 'Reserva Confirmada'),
        ('CANCELADO', 'Cancelado'),
        ('FINALIZADO', 'Evento Realizado'),
    ]

    # --- DADOS PREENCHIDOS PELO CLIENTE ---
    nome_cliente = models.CharField(max_length=100, verbose_name="Nome do Cliente")
    data_evento = models.DateTimeField(verbose_name="Data e Hora do Evento")
    tipo_evento = models.CharField(max_length=100, help_text="Ex: Aniversário, Corporativo", verbose_name="Tipo de Evento")
    numero_pessoas = models.IntegerField(verbose_name="Nº de Pessoas")
    telefone_whatsapp = models.CharField(max_length=20, verbose_name="WhatsApp")
    email_cliente = models.EmailField(verbose_name="E-mail")

    # --- DADOS INTERNOS (GIARDINI) ---
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name="Data do Pedido")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDENTE')
    
    # Detalhes acertados após contato
    valor_acertado = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Valor Total (R$)")
    local_giardini = models.CharField(max_length=100, null=True, blank=True, verbose_name="Local Definido")
    tema_decoracao = models.CharField(max_length=200, null=True, blank=True, verbose_name="Tema da Decoração")
    coffee_break = models.TextField(null=True, blank=True, verbose_name="Itens do Coffee Break")

    def __str__(self):
        return f"{self.nome_cliente} - {self.data_evento.strftime('%d/%m %H:%M')}"

    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"