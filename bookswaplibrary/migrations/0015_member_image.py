# Generated by Django 4.1.6 on 2023-06-14 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookswaplibrary', '0014_bookinstance_exchange_preference_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/profileimages'),
        ),
    ]
