# Generated by Django 4.2.4 on 2023-09-11 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SSLCertificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(max_length=255)),
                ('issuer', models.CharField(max_length=255)),
                ('valid_until', models.DateField()),
            ],
        ),
    ]
