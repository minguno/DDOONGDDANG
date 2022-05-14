# Generated by Django 3.2.12 on 2022-05-14 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20220514_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(error_messages={'unique': '이미 존재하는 이메일입니다.'}, max_length=254),
        ),
    ]