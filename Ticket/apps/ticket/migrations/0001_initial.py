# Generated by Django 4.2.16 on 2024-10-26 12:16

import Ticket.apps.ticket.abstract_models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('id', models.CharField(default=Ticket.apps.ticket.abstract_models.AbstractTicket.auto_generate_id, editable=False, max_length=35, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('contact_info', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('pending', 'รอดำเนินการ'), ('accepeted', 'รับเรื่องแล้ว'), ('resolved', 'ดำเนินการแก้ไขแล้ว'), ('rejected', 'ถูกปฏิเสธ')], default='pending', max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TicketLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('action', models.CharField(max_length=255)),
                ('previous_status', models.CharField(blank=True, max_length=50, null=True)),
                ('new_status', models.CharField(blank=True, max_length=50, null=True)),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='ticket.ticket')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
