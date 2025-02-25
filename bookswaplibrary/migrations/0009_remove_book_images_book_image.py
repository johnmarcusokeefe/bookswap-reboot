# Generated by Django 4.1.6 on 2023-05-19 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookswaplibrary', '0008_remove_bookimage_book_book_images_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='images',
        ),
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/bookimages'),
        ),
    ]
