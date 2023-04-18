# Generated by Django 4.2 on 2023-04-18 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mercado', '0002_lista_remove_mercado_code_remove_produtos_code_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Mercado',
        ),
        migrations.RemoveField(
            model_name='produtos',
            name='produto',
        ),
        migrations.AddField(
            model_name='produtos',
            name='lista',
            field=models.ManyToManyField(blank=True, related_name='produtos', to='mercado.lista'),
        ),
        migrations.AddField(
            model_name='produtos',
            name='nome',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produtos',
            name='preco',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
