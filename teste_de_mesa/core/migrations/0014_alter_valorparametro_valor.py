# Generated by Django 4.0.5 on 2022-07-02 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_dicionarioparametros_valorparametro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='valorparametro',
            name='valor',
            field=models.CharField(db_index=True, max_length=240, null=True),
        ),
    ]