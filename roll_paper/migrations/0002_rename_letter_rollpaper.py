# Generated by Django 3.2.12 on 2022-04-28 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('roll_paper', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Letter',
            new_name='RollPaper',
        ),
    ]
