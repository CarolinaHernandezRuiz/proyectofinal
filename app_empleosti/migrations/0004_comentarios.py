# Generated by Django 4.0.3 on 2022-03-23 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_empleosti', '0003_remove_empleo_imagen_remove_empleo_titulo_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('telefono', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=150)),
                ('comentario', models.TextField()),
            ],
        ),
    ]