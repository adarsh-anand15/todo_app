# Generated by Django 2.1 on 2018-08-21 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0004_auto_20180822_0100'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todolist',
            options={'get_latest_by': ['-due_date']},
        ),
    ]
