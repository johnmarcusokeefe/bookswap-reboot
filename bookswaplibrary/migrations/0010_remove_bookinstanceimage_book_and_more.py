# Generated by Django 4.1.6 on 2023-05-20 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookswaplibrary', '0009_remove_book_images_book_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookinstanceimage',
            name='book',
        ),
        migrations.AddField(
            model_name='bookinstance',
            name='condition_notes',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='bookinstance',
            name='images',
            field=models.ManyToManyField(to='bookswaplibrary.bookinstanceimage'),
        ),
    ]
