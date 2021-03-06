# Generated by Django 3.2.12 on 2022-02-11 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='caveinventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=150)),
                ('region', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=150)),
                ('barangay', models.CharField(max_length=150)),
                ('sitio_purok', models.CharField(max_length=100)),
                ('remark', models.TextField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
        ),
    ]
