# Generated by Django 4.1.6 on 2023-05-16 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookswaplibrary', '0006_remove_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/bookimages'),
        ),
        migrations.AlterField(
            model_name='bookinstanceimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/bookinstanceimages'),
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
