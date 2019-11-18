# Generated by Django 2.2.7 on 2019-11-18 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='question',
            name='level',
            field=models.CharField(blank=True, choices=[('easy', 'easy'), ('normal', 'normal'), ('hard', 'hard')], max_length=50, null=True),
        ),
    ]
