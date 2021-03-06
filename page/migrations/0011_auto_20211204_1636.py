# Generated by Django 3.2.9 on 2021-12-04 15:36

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0010_blogpost_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='category',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='category',
            field=models.ManyToManyField(to='page.BlogCategory'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, default=None, editable=False, null=True, populate_from='title', unique=True),
        ),
    ]
