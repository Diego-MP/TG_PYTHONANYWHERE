# Generated by Django 4.1 on 2022-08-30 00:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_produtos_imagem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chamados',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('defeito', models.TextField(blank=True, max_length=255, null=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.clientes')),
            ],
        ),
    ]
