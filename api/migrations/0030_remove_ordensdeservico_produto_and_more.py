# Generated by Django 4.1 on 2022-10-25 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0029_ordensdeservico_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordensdeservico',
            name='produto',
        ),
        migrations.AlterField(
            model_name='ordensdeservico',
            name='peca',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Peça'),
        ),
    ]
