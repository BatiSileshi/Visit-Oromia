# Generated by Django 3.2 on 2022-09-30 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system_admin', '0007_alter_place_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='photo',
            field=models.ImageField(blank=True, max_length=55, null=True, upload_to=''),
        ),
    ]
