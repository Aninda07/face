# Generated by Django 4.0.6 on 2022-07-28 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0035_alter_contact_birthdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='Birthdate',
            field=models.IntegerField(default=2022),
        ),
    ]
