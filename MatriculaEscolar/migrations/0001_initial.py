# Generated by Django 4.1.2 on 2022-11-14 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MatriculaEscolares',
            fields=[
                ('ano', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('Nmatriculados', models.PositiveIntegerField()),
                ('preescolar', models.PositiveIntegerField()),
                ('primaria', models.PositiveIntegerField()),
                ('basicaSecundarioa', models.PositiveIntegerField()),
                ('media', models.PositiveIntegerField()),
            ],
        ),
    ]
