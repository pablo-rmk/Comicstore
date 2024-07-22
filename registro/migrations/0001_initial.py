# Generated by Django 5.0.6 on 2024-06-06 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id_ciudad', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre_ciudad', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('rut', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('nombre_usuario', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=200)),
                ('id_ciudad', models.CharField(max_length=10)),
                ('id_pais', models.CharField(max_length=10)),
                ('id_comuna', models.CharField(max_length=10)),
                ('codigo_postal', models.CharField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id_comuna', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre_comuna', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id_pais', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre_pais', models.CharField(max_length=100)),
            ],
        ),
    ]
