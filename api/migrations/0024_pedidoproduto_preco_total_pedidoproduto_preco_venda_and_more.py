# Generated by Django 4.1 on 2022-10-21 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_pedidodevenda_contato_venda_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedidoproduto',
            name='preco_total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='pedidoproduto',
            name='preco_venda',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='pedidoproduto',
            name='quantidade',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]