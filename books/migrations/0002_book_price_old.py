# Generated by Django 2.2.7 on 2019-11-19 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price_old',
            field=models.DecimalField(decimal_places=2, default=99.99, max_digits=10),
            preserve_default=False,
        ),
    ]