# Generated by Django 4.2.7 on 2023-11-13 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_group_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='subgroup',
            field=models.SmallIntegerField(blank=True, default=1, verbose_name='Подгруппа'),
        ),
    ]
