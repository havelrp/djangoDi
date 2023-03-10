# Generated by Django 4.1.2 on 2023-02-28 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('dni', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('fecha_nacimiento', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('dimension', models.CharField(max_length=50)),
                ('material', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('precio', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('cantidad', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hous3d.cliente')),
                ('modelo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hous3d.modelo')),
            ],
        ),
    ]
