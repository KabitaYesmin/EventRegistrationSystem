# Generated by Django 5.0.1 on 2024-01-04 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_events_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='description',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='events',
            name='location',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
