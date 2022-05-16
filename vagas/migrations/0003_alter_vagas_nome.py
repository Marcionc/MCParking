# Generated by Django 3.2.13 on 2022-05-16 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamento', '0002_alter_estacionamento_nome'),
        ('vagas', '0002_alter_vagas_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vagas',
            name='nome',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estacionamento.estacionamento', verbose_name='Estacionamento'),
        ),
    ]