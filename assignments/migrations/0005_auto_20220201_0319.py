# Generated by Django 3.1.4 on 2022-01-31 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0004_assignment_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='file',
            field=models.FileField(upload_to='media'),
        ),
    ]