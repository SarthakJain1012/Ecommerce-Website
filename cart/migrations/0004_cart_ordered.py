# Generated by Django 3.2.4 on 2021-06-29 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_cartitem_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='ordered',
            field=models.BooleanField(default=False),
        ),
    ]
