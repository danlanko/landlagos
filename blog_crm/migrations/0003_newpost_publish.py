# Generated by Django 2.2.4 on 2019-08-19 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_crm', '0002_auto_20190819_1057'),
    ]

    operations = [
        migrations.AddField(
            model_name='newpost',
            name='publish',
            field=models.BooleanField(default=True),
        ),
    ]
