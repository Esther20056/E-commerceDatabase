# Generated by Django 5.1.3 on 2024-12-08 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='color',
            field=models.CharField(default='color', max_length=20),
        ),
    ]
