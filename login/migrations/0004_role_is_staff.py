# Generated by Django 4.1.5 on 2023-01-28 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_shippingaddress_member_shippingaddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
