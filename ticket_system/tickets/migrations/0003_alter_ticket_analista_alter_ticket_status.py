# Generated by Django 5.1.6 on 2025-02-20 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_remove_ticket_descricao_remove_ticket_titulo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='analista',
            field=models.CharField(choices=[('Leandro Fratel', 'Leandro Fratel'), ('Heráclito Teixeira', 'Heráclito Teixeira'), ('Camilla Gama', 'Camilla Gama')], default='', max_length=100, verbose_name='Analista'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('Aberto', 'Aberto'), ('Fechado', 'Fechado'), ('Resolvido', 'Resolvido'), ('Em Andamento', 'Em Andamento'), ('Designado', 'Designado'), ('Em Análise', 'Em Análise'), ('Sala de Crise', 'Sala de Crise')], default='Aberto', max_length=50, verbose_name='Status'),
        ),
    ]
