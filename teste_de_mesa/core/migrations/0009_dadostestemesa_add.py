# Generated by Django 4.0.5 on 2022-06-28 17:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_dadostestemesa_linha'),
    ]

    operations = [
        migrations.AddField(
            model_name='dadostestemesa',
            name='add',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Adicionado'),
            preserve_default=False,
        ),
    ]
