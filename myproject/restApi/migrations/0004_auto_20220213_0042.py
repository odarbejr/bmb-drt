# Generated by Django 3.2.12 on 2022-02-12 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restApi', '0003_geographic_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='climatological_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rainfall_pattern', models.CharField(blank=True, max_length=100, null=True)),
                ('climate_type', models.CharField(blank=True, max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='caveinventory',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='caveinventory',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='geographic_description',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='geographic_description',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='period_accessment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='period_accessment',
            name='total_days',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='period_accessment',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
