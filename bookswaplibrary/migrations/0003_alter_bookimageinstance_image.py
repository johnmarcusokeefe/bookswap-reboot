# Generated by Django 4.1.6 on 2023-05-15 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookswaplibrary', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookimageinstance',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/bookinstanceimages'),
        ),
    ]
