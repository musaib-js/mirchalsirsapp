# Generated by Django 3.1.4 on 2022-01-31 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0015_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='resource',
            field=models.FileField(upload_to='media/resource'),
        ),
        migrations.AlterField(
            model_name='course',
            name='thumbnail',
            field=models.ImageField(upload_to='media/thumbnail'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='picture',
            field=models.ImageField(upload_to='media/teachers'),
        ),
    ]
