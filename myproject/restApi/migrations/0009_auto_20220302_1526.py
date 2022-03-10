# Generated by Django 3.2.12 on 2022-03-02 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restApi', '0008_auto_20220224_1125'),
    ]

    operations = [
        migrations.CreateModel(
            name='region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=9)),
                ('name', models.CharField(max_length=200)),
                ('region_id', models.CharField(max_length=5)),
            ],
        ),
        migrations.AlterField(
            model_name='caveinventory',
            name='city',
            field=models.CharField(choices=[('Adams', 'Adams'), ('Bacarra', 'Bacarra'), ('Badoc', 'Badoc'), ('Bangui', 'Bangui'), ('City of Bata', 'City of Batac'), ('Burgos', 'Burgos'), ('Carasi', 'Carasi'), ('Currimao', 'Currimao'), ('Dingras', 'Dingras'), ('Dumalneg', 'Dumalneg'), ('Banna', 'Banna'), ('City of Laoag (Capital)', 'City of Laoag (Capital)'), ('Marcos', 'Marcos'), ('Nueva Era', 'Nueva Era'), ('Pagudpud', 'Pagudpud'), ('Paoay', 'Paoay'), ('Pasuquin', 'Pasuquin'), ('Piddig', 'Piddig'), ('Pinili', 'Pinili'), ('San Nicolas', 'San Nicolas'), ('Sarrat', 'Sarrat')], max_length=150),
        ),
        migrations.AlterField(
            model_name='caveinventory',
            name='region',
            field=models.CharField(choices=[('Ilocos', 'Ilocos'), ('Cagayan Valley', 'Cagayan Valley'), ('Central Luzon', 'Central Luzon'), ('Calabarzon', 'Calabarzon'), ('Mimaropa', 'Mimaropa'), ('Bicol Region', 'Bicol Region'), ('Western Visayas', 'Western Visayas'), ('Central Visayas', 'Central Visayas'), ('Eastern Visayas', 'Eastern Visayas'), ('Zamboanga Peninsula', 'Zamboanga Peninsula'), ('Northern Mindanao', 'Northern Mindanao'), ('Davao', 'Davao'), ('SOCCSKSARGEN', 'SOCCSKSARGEN'), ('Caraga', 'Caraga'), ('National Capital Region', 'National Capital Region'), ('Cordillera Administrative Region', 'Cordillera Administrative Region'), ('Bangsamoro Autonomous Region in Muslim Mindanao', 'Bangsamoro Autonomous Region in Muslim Mindanao'), ('Zamboanga Peninsula', 'Zamboanga Peninsula')], max_length=150),
        ),
        migrations.AlterField(
            model_name='layers_attribute',
            name='region',
            field=models.CharField(blank=True, choices=[('Ilocos', 'Ilocos'), ('Cagayan Valley', 'Cagayan Valley'), ('Central Luzon', 'Central Luzon'), ('Calabarzon', 'Calabarzon'), ('Mimaropa', 'Mimaropa'), ('Bicol Region', 'Bicol Region'), ('Western Visayas', 'Western Visayas'), ('Central Visayas', 'Central Visayas'), ('Eastern Visayas', 'Eastern Visayas'), ('Zamboanga Peninsula', 'Zamboanga Peninsula'), ('Northern Mindanao', 'Northern Mindanao'), ('Davao', 'Davao'), ('SOCCSKSARGEN', 'SOCCSKSARGEN'), ('Caraga', 'Caraga'), ('National Capital Region', 'National Capital Region'), ('Cordillera Administrative Region', 'Cordillera Administrative Region'), ('Bangsamoro Autonomous Region in Muslim Mindanao', 'Bangsamoro Autonomous Region in Muslim Mindanao'), ('Zamboanga Peninsula', 'Zamboanga Peninsula')], max_length=80, null=True),
        ),
    ]