# Generated by Django 4.1 on 2022-09-30 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_alter_produtos_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos',
            name='estoque',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]