# Generated by Django 4.1 on 2022-10-24 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_pedidoproduto_preco_total_pedidoproduto_preco_venda_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordensdeservico',
            name='peca',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Equipamento'),
        ),
        migrations.AddField(
            model_name='ordensdeservico',
            name='valor',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True),
        ),
    ]
