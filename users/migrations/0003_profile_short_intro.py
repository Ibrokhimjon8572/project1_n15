# Generated by Django 4.2.5 on 2023-10-09 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='short_intro',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
