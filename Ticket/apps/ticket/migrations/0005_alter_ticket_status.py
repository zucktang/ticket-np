# Generated by Django 4.2.16 on 2024-11-01 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0004_ticket_expire_date_ticket_image_ticket_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('pending', 'รอดำเนินการ'), ('accepted', 'รับเรื่องแล้ว'), ('resolved', 'ดำเนินการแก้ไขแล้ว'), ('rejected', 'ถูกปฏิเสธ')], default='pending', max_length=50),
        ),
    ]
