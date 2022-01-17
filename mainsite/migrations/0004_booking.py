# Generated by Django 3.2 on 2022-01-17 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0003_auto_20220113_1633'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('date', models.DateField(blank=True, null=True)),
                ('sent_date', models.DateField(auto_now_add=True)),
                ('accepted', models.BooleanField(default=False)),
                ('accepted_date', models.DateTimeField(null=True)),
                ('time', models.CharField(choices=[('08:00-09:00', '08:00 to 09:00'), ('09:00-10:00', '09:00 to 10:00'), ('10:00-11:00', '10:00 to 11:00'), ('11:00-12:00', '11:00 to 12:00'), ('12:00-13:00', '12:00 to 13:00'), ('13:00-14:00', '13:00 to 14:00'), ('14:00-15:00', '14:00 to 15:00'), ('15:00-16:00', '15:00 to 16:00'), ('16:00-17:00', '16:00 to 17:00')], default='08:00-09:00', max_length=50)),
                ('addinfo', models.TextField(blank=True, max_length=1000)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainsite.client')),
            ],
            options={
                'ordering': ['-sent_date'],
            },
        ),
    ]