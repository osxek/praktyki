# Generated by Django 4.2.5 on 2023-09-19 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssl_checker_app', '0007_alter_userprofile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
