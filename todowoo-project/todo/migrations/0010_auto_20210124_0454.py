# Generated by Django 3.1.4 on 2021-01-24 04:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0009_auto_20210124_0244'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projecttodowooflo',
            old_name='creator',
            new_name='user',
        ),
    ]
