# Generated by Django 2.2.24 on 2021-07-28 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0029_allowlist_created_20210623_1417'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CertificateWhitelist',
        ),
    ]