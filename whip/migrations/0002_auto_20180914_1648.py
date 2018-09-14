# Generated by Django 2.1 on 2018-09-14 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whip', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='bidderReceivedPoints',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=0),
        ),
    ]
