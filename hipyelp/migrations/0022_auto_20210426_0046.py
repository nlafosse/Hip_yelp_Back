# Generated by Django 3.2 on 2021-04-26 00:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hipyelp', '0021_auto_20210426_0031'),
    ]

    operations = [
        migrations.RenameField(
            model_name='drinktag',
            old_name='tagname',
            new_name='tags',
        ),
        migrations.RenameField(
            model_name='foodtag',
            old_name='tagname',
            new_name='tags',
        ),
    ]
