# Generated by Django 4.1.3 on 2022-11-07 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_city_locality_userrole'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='is_author',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='is_user',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]