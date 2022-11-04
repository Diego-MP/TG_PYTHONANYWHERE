# Generated by Django 4.1 on 2022-10-22 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_front', '0002_empresa_site'),
    ]

    operations = [
        migrations.CreateModel(
            name='VendaAUX',
            fields=[
                ('id_venda', models.AutoField(primary_key=True, serialize=False)),
                ('id_cliente', models.IntegerField(blank=True, null=True)),
                ('id_produto', models.IntegerField(blank=True, null=True)),
                ('valor', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('quantidade', models.IntegerField(blank=True, null=True)),
                ('valor_total', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
            ],
        ),
    ]