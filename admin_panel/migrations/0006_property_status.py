# Generated by Django 4.0.2 on 2022-05-13 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0005_property'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='status',
            field=models.CharField(max_length=12, null=True),
        ),
    ]
