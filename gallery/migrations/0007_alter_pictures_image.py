# Generated by Django 5.0.2 on 2024-02-24 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0006_alter_pictures_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pictures',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/%y'),
        ),
    ]
