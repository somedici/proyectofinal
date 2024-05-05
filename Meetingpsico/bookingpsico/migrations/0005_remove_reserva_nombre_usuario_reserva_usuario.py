# Generated by Django 5.0.4 on 2024-05-05 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingpsico', '0004_remove_reserva_usuario_delete_customuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='nombre_usuario',
        ),
        migrations.AddField(
            model_name='reserva',
            name='usuario',
            field=models.CharField(default='usuario_predeterminado', max_length=100),
            preserve_default=False,
        ),
    ]
