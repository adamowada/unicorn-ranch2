# Generated by Django 4.0.4 on 2022-05-04 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_unicorn_color_alter_unicorn_location_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='unicorn',
            options={'ordering': ['name']},
        ),
    ]
