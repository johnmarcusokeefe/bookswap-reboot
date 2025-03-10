# Generated by Django 4.1.6 on 2023-06-08 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookswaplibrary', '0012_remove_bookinstance_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='condition',
            field=models.CharField(choices=[('excellent', 'Excellent'), ('good', 'Good'), ('bad', 'Bad'), ('dog_eared', 'Dog Eared'), ('water_damaged', 'Water Damaged'), ('missing_pages', 'Missing Pages')], max_length=20),
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='status',
            field=models.CharField(choices=[('on_load', 'On loan'), ('available', 'Available'), ('unavailable', 'Unavailable'), ('reserved', 'Reserved')], max_length=20),
        ),
    ]
