# Generated by Django 2.0.3 on 2018-04-07 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapp', '0003_auto_20180407_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='profile_pic',
            field=models.ImageField(upload_to='user_pics'),
        ),
    ]
