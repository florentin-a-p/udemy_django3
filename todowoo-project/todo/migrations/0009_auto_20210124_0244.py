# Generated by Django 3.1.4 on 2021-01-24 02:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0008_auto_20210124_0243'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projecttodowooflo',
            old_name='user',
            new_name='creator',
        ),
    ]