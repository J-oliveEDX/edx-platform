# Generated by Django 2.2.19 on 2021-02-23 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_overviews', '0023_courseoverview_banner_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseoverview',
            name='has_highlights',
            field=models.BooleanField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='historicalcourseoverview',
            name='has_highlights',
            field=models.BooleanField(default=None, null=True),
        ),
    ]
