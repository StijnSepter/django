# Generated by Django 4.2.6 on 2024-02-08 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_skill_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='text',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]