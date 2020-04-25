# Generated by Django 3.0.5 on 2020-04-24 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20200424_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='botaplication',
            name='button_size',
            field=models.IntegerField(choices=[(10, 10), (20, 20), (30, 30), (50, 50)], default=10, verbose_name='Tamaño del ícono'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='botaplication',
            name='name',
            field=models.CharField(default='Bot App', max_length=160, verbose_name='Nombre'),
        ),
    ]