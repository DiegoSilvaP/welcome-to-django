# Generated by Django 3.0.5 on 2020-04-24 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20200424_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='botaplication',
            name='is_enabled',
            field=models.BooleanField(db_index=True, default=False, verbose_name='Activado'),
        ),
    ]
