# Generated by Django 3.2 on 2022-01-17 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0009_alter_client_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteuser',
            name='number',
            field=models.CharField(max_length=11, null=True),
        ),
    ]