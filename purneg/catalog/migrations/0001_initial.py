# Generated by Django 4.0.2 on 2022-02-04 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('number', models.CharField(max_length=20)),
                ('date', models.DateField(max_length=20)),
                ('url', models.CharField(max_length=20)),
            ],
        ),
    ]
