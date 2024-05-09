# Generated by Django 5.0.6 on 2024-05-08 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='termdeposit',
            name='deposit_amount',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
        migrations.AlterField(
            model_name='termdeposit',
            name='interest_rate',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
        migrations.AlterField(
            model_name='termdeposit',
            name='term',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
    ]
