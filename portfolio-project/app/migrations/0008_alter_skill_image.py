# Generated by Django 4.2.6 on 2024-02-07 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_skill_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='image',
            field=models.TextField(editable=False),
        ),
    ]
