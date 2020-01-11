# Generated by Django 2.0 on 2020-01-04 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0011_politicalparty_president'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voting',
            name='tipe',
            field=models.TextField(choices=[('PP', 'Presidential primaries'), ('SP', 'Senate primaries'), ('S', 'Senate'), ('P', 'Presidential')], verbose_name='Type'),
        ),
    ]
