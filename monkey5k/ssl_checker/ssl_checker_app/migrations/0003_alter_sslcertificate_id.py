# Generated by Django 4.2.4 on 2023-09-13 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssl_checker_app', '0002_remove_sslcertificate_issuer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sslcertificate',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]