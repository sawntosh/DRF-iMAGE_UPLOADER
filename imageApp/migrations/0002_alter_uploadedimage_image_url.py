# Generated by Django 4.2 on 2023-05-04 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedimage',
            name='image_url',
            field=models.ImageField(upload_to='uploads/'),
        ),
    ]
