# Generated by Django 5.0.6 on 2024-07-16 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='emp',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('phone', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('working', models.BooleanField(default=True)),
                ('department', models.CharField(max_length=10)),
            ],
        ),
    ]
