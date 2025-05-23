# Generated by Django 4.1 on 2025-04-24 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pensionado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('edad', models.IntegerField(default=0)),
                ('edadRetiro', models.IntegerField(default=70)),
                ('saldo', models.FloatField(default=500000.0)),
                ('ahorro', models.FloatField(default=10000.0)),
                ('genero', models.BooleanField(default=False)),
            ],
        ),
    ]
