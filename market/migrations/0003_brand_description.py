# Generated by Django 5.1.3 on 2024-12-07 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_alter_category_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
