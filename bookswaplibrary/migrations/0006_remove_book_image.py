# Generated by Django 4.1.6 on 2023-05-16 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookswaplibrary', '0005_bookimage_bookinstanceimage_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='image',
        ),
    ]
