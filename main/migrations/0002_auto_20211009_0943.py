# Generated by Django 3.2.8 on 2021-10-09 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gemotest',
            name='generate_number',
            field=models.IntegerField(default=32720504),
        ),
        migrations.AlterField(
            model_name='gemotest',
            name='number_of_passport',
            field=models.CharField(max_length=20),
        ),
    ]
