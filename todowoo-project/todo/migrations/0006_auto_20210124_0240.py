# Generated by Django 3.1.4 on 2021-01-24 02:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_auto_20210124_0233'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projecttodowooflo',
            old_name='user_name',
            new_name='usercreator',
        ),
    ]
