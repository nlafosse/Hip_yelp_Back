# Generated by Django 3.2 on 2021-04-25 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hipyelp', '0022_auto_20210425_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodtag',
            name='tagname',
            field=models.TextField(),
        ),
    ]
