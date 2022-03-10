from django.db import models
# from django.contrib.auth.models import User

# Create your models here.

REGION_SELECTION = [
    ('Ilocos', 'Ilocos'),
    ('Cagayan Valley', 'Cagayan Valley'),
    ('Central Luzon', 'Central Luzon'),
    ('Calabarzon', 'Calabarzon'),
    ('Mimaropa', 'Mimaropa'),
    ('Bicol Region', 'Bicol Region'),
    ('Western Visayas', 'Western Visayas'),
    ('Central Visayas', 'Central Visayas'),
    ('Eastern Visayas', 'Eastern Visayas'),
    ('Zamboanga Peninsula', 'Zamboanga Peninsula'),
    ('Northern Mindanao', 'Northern Mindanao'),
    ('Davao', 'Davao'),
    ('SOCCSKSARGEN', 'SOCCSKSARGEN'),
    ('Caraga', 'Caraga'),
    ('National Capital Region', 'National Capital Region'),
    ('Cordillera Administrative Region', 'Cordillera Administrative Region'),
    ('Bangsamoro Autonomous Region in Muslim Mindanao', 'Bangsamoro Autonomous Region in Muslim Mindanao'),
]
CITIES_SELECTION = [
    ('Adams','Adams'),
    ('Bacarra','Bacarra'),
    ('Badoc','Badoc'),
    ('Bangui','Bangui'),
    ('City of Bata','City of Batac'),
    ('Burgos','Burgos'),
    ('Carasi','Carasi'),
    ('Currimao','Currimao'),
    ('Dingras','Dingras'),
    ('Dumalneg','Dumalneg'),
    ('Banna','Banna'),
    ('City of Laoag (Capital)','City of Laoag (Capital)'),
    ('Marcos','Marcos'),
    ('Nueva Era','Nueva Era'),
    ('Pagudpud','Pagudpud'),
    ('Paoay','Paoay'),
    ('Pasuquin','Pasuquin'),
    ('Piddig','Piddig'),
    ('Pinili','Pinili'),
    ('San Nicolas','San Nicolas'),
    ('Sarrat','Sarrat'),
    
]


class region(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    code = models.CharField(max_length=9)
    name = models.CharField(max_length=200)
    region_id = models.CharField(max_length=5)
 
def __str__(self):
    return "%s"%(self.id)

class cities(models.Model):
    code = models.CharField(max_length=9)
    name = models.CharField(max_length=200)
    region_id = models.CharField(max_length=5)
    province_id = models.CharField(max_length=10)
    city_id = models.CharField(max_length=10)
 
def __str__(self):
    return "%s"%(self.id)
    

class caveinventory(models.Model):
    cname = models.CharField(max_length=150)
    region = models.CharField(max_length=150,choices=REGION_SELECTION)
    city = models.CharField(max_length=150,choices=CITIES_SELECTION)
    barangay = models.CharField(max_length=150)
    sitio_purok = models.CharField(max_length=100)
    remark = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
def __str__(self):
    return "%s"%(self.id) 

class Period_accessment(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    total_days = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
def __str__(self):
    return self.start_date

class Geographic_description(models.Model):
    latitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)
    elevation = models.CharField(max_length=100)
    evolution_of_cave = models.CharField(max_length=100)
    land_status = models.CharField(max_length=100)
    accessibility = models.TextField()
    others = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
def __str__(self):
    return self.latitude

class climatological_data(models.Model):
    rainfall_pattern = models.CharField(max_length=100, null=True, blank=True)
    climate_type = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
def __str__(self):
    return self.rainfall_pattern

class excisting_land_use(models.Model):
    listing_by_type = models.CharField(max_length=50, null=True, blank=True)
    adjacent_to_cave = models.TextField(null=True, blank=True)
    above_cave = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
def __str__(self):
    return self.listing_by_type

class demographic_information(models.Model):
    name_brgy = models.CharField(max_length=100, null=True, blank=True)
    population = models.CharField(max_length=50, null=True, blank=True)
    households = models.CharField(max_length=50, null=True, blank=True)
    families = models.CharField(max_length=50, null=True, blank=True)
    livelihood = models.CharField(max_length=80, null=True, blank=True)
    others = models.CharField(max_length=80, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
def __str__(self):
    return self.name_brgy

class uses(models.Model):
    type_of_activity = models.CharField(max_length=100, null=True, blank=True)
    implementation_period = models.CharField(max_length=100, null=True, blank=True)
    station_covered = models.CharField(max_length=50, null=True, blank=True)
    implementing_agencies = models.CharField(max_length=155, null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
def __str__(self):
    return self.type_of_activity

class Type_of_animals(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=150, null=True, blank=True)
    image = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

def __str__(self):
    return "%s"%(self.id)

ANIMALS_SELECTION = [
    ('Troglobites','Troglobites'),
    ('Troglophiles','Troglophiles'),
    ('Accidentals ','Accidentals '),
    ('Infrared eyesight ','Infrared eyesight '),
    ('Giant centipedes ','Giant centipedes '),
    ('elephantnose fish','elephantnose fish'),
]

SIZE_SELECTION = [
    ('L', 'Large'),
    ('M', 'Meduim'),
    ('S', 'Small'),
    ('NS', 'Not Specified'),
]

class Layers_attribute(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    layer_name = models.CharField(max_length=100, null=True, blank=True)
    description= models.CharField(max_length=100, null=True, blank=True)
    region= models.CharField(max_length=80, null=True, blank=True, choices=REGION_SELECTION)
    barangay= models.CharField(max_length=100, null=True, blank=True)
    city= models.CharField(max_length=100, null=True, blank=True)
    total_of_cave= models.IntegerField(null=True, blank=True)
    type_of_animal = models.CharField(max_length=100, null=True, blank=True, choices=ANIMALS_SELECTION)
    total_of_male= models.IntegerField(null=True, blank=True)
    total_of_female= models.IntegerField(null=True, blank=True)
    overall_gender= models.IntegerField(null=True, blank=True)
    size= models.CharField(max_length=20, choices=SIZE_SELECTION)
    color= models.CharField(max_length=50, null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   
    # class Meta:
    #     db_table="restApi_layers_attribute" 
 
def __str__(self):
    return self.layer_name
    #  return '%d: %s' % (self.layer_name, self.description)


