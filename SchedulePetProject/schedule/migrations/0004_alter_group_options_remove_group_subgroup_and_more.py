# Generated by Django 4.2.7 on 2023-11-13 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0003_group_subgroup'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'ordering': ('title',), 'verbose_name': 'Группа', 'verbose_name_plural': 'Группы'},
        ),
        migrations.RemoveField(
            model_name='group',
            name='subgroup',
        ),
        migrations.AddField(
            model_name='schedule',
            name='session',
            field=models.CharField(default=1, max_length=128, verbose_name='Пара'),
        ),
    ]
