# Generated by Django 4.2.1 on 2023-07-25 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaProd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('origen', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=400)),
                ('frase', models.CharField(max_length=100)),
                ('foto', models.ImageField(upload_to='quienes')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Colma2',
                'verbose_name_plural': 'Colma2',
            },
        ),
    ]
