# Generated by Django 4.0.5 on 2022-06-28 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_palavrareservada'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PalavraReservada',
        ),
        migrations.RemoveField(
            model_name='dadostestemesa',
            name='dado_hexa_o',
        ),
        migrations.RemoveField(
            model_name='dadostestemesa',
            name='num_equacao',
        ),
        migrations.RemoveField(
            model_name='dadostestemesa',
            name='variavel_o',
        ),
    ]
