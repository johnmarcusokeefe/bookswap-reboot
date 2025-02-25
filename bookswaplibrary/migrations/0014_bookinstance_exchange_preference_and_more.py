# Generated by Django 4.1.6 on 2023-06-11 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookswaplibrary', '0013_alter_bookinstance_condition_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinstance',
            name='exchange_preference',
            field=models.CharField(choices=[('swap', 'Swap'), ('loan', 'Loan'), ('gift', 'Gift')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='status',
            field=models.CharField(choices=[('on_loan', 'On loan'), ('available', 'Available'), ('unavailable', 'Unavailable'), ('reserved', 'Reserved')], max_length=20),
        ),
    ]
