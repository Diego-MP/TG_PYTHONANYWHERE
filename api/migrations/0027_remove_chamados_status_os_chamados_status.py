# Generated by Django 4.1 on 2022-10-25 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_chamados_status_os'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chamados',
            name='status_os',
        ),
        migrations.AddField(
            model_name='chamados',
            name='status',
            field=models.CharField(blank=True, choices=[('1', 'Pendente'), ('2', 'Manutencao'), ('3', 'Finalizada')], max_length=2, null=True),
        ),
    ]
