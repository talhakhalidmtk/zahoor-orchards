# Generated by Django 4.0.4 on 2022-05-12 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0003_alter_client_cnic'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='status',
            field=models.CharField(max_length=12, null=True),
        ),
    ]