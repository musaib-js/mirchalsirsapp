# Generated by Django 3.1.4 on 2022-01-30 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0003_auto_20220129_2127'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='difficluty',
            field=models.CharField(choices=[('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')], max_length=6),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='required_score_to_pass',
            field=models.IntegerField(help_text='Required score in %'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='time',
            field=models.IntegerField(help_text='Duration of the quiz in minutes'),
        ),
    ]
