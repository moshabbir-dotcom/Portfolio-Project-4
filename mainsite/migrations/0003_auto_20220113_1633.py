# Generated by Django 3.2 on 2022-01-13 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0002_rename_clients_client'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='passwrd',
        ),
        migrations.AddField(
            model_name='client',
            name='number',
            field=models.CharField(max_length=16, null=True),
        ),
    ]