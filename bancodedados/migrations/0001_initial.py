# Generated by Django 4.2.2 on 2023-06-28 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('identificador', models.AutoField(primary_key=True, serialize=False)),
                ('quantidade', models.PositiveIntegerField()),
                ('descricao', models.TextField()),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
    ]
