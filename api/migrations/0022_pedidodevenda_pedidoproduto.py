# Generated by Django 4.1 on 2022-10-19 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_produtos_imagem_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='PedidoDeVenda',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.clientes')),
            ],
        ),
        migrations.CreateModel(
            name='PedidoProduto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.pedidodevenda')),
                ('id_produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.produtos')),
            ],
        ),
    ]
