# Generated by Django 3.1.7 on 2021-07-16 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210716_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='is_publish',
            field=models.BooleanField(choices=[(True, 'publish'), (False, 'draft')], default=False, max_length=10),
        ),
    ]