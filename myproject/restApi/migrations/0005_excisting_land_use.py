# Generated by Django 3.2.12 on 2022-02-13 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restApi', '0004_auto_20220213_0042'),
    ]

    operations = [
        migrations.CreateModel(
            name='excisting_land_use',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listing_by_type', models.CharField(blank=True, max_length=50, null=True)),
                ('adjacent_to_cave', models.TextField(blank=True, null=True)),
                ('above_cave', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
