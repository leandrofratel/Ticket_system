# Generated by Django 5.1.6 on 2025-02-20 17:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_alter_ticket_analista_alter_ticket_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='imagens',
        ),
        migrations.AlterField(
            model_name='ticket',
            name='recurso',
            field=models.CharField(max_length=50, verbose_name='Recurso'),
        ),
        migrations.CreateModel(
            name='TicketImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='tickets/images/')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='tickets.ticket')),
            ],
        ),
    ]
