# Generated by Django 4.1 on 2022-09-02 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_chamados_data_criacao_chamados_data_modificacao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordensdeservico',
            name='produto',
            field=models.ManyToManyField(to='api.produtos'),
        ),
    ]
