# Generated by Django 4.0.5 on 2022-07-02 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_casoteste_add'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testemesa',
            name='fk_dados',
        ),
        migrations.AddField(
            model_name='dadostestemesa',
            name='fk_teste',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.testemesa'),
            preserve_default=False,
        ),
    ]