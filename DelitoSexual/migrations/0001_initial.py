# Generated by Django 4.1.2 on 2022-11-14 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DelitoSexuales',
            fields=[
                ('ano', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('Ncasos', models.PositiveIntegerField()),
                ('hombres', models.PositiveIntegerField()),
                ('mujeres', models.PositiveIntegerField()),
            ],
        ),
    ]