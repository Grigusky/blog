# Generated by Django 3.2.9 on 2021-12-03 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0005_alter_blogpost_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='category',
            new_name='article',
        ),
    ]
