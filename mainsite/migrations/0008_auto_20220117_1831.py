# Generated by Django 3.2 on 2022-01-17 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0007_auto_20220117_1506'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('passwrd', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='booking',
            name='treatment',
            field=models.CharField(choices=[('physical_therapy', 'Physical Therapy -£45'), ('sports_massage_therapy', 'Sports Massage Therapy -£45'), ('fire_cupping_therapy', 'Fire Cupping Therapy -£50'), ('swedish_massage_therapy', 'Swedish Massage Therapy -£45'), ('aroma_therapy', 'Aromatherapy -£45'), ('wet_cupping_therapy', 'Wet Cupping Therapy -£45'), ('graston_therapy', 'Graston IATM Therapy -£45'), ('nutrition_therapy', 'Nutritional Therapy -£45')], default='Physical Therapy -£45', max_length=100),
        ),
        migrations.AlterField(
            model_name='client',
            name='number',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainsite.siteuser'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainsite.siteuser'),
        ),
    ]
