# Generated by Django 3.2.8 on 2021-10-08 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_gemotest_generate_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gemotest',
            name='generate_number',
            field=models.IntegerField(default=71496163),
        ),
    ]
