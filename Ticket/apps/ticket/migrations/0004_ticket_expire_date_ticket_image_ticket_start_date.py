# Generated by Django 4.2.16 on 2024-11-01 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0003_alter_ticketlog_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='expire_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='ticket_images/'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
