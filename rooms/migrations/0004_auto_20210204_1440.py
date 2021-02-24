# Generated by Django 3.1.5 on 2021-02-04 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0003_auto_20210204_1439'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Facilty',
            new_name='Facility',
        ),
        migrations.AddField(
            model_name='room',
            name='facilities',
            field=models.ManyToManyField(to='rooms.Facility'),
        ),
        migrations.AddField(
            model_name='room',
            name='house_rules',
            field=models.ManyToManyField(to='rooms.HouseRule'),
        ),
    ]