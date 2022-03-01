from django.db import models
# from django.contrib.auth.models import User

# Create your models here.

REGION_SELECTION = [
    ('Region I', 'Ilocos Region'),
    ('Region II', 'Cagayan Valley'),
    ('Region III', 'Central Luzon'),
    ('Region IV', 'Calabarzon'),
    ('Region', 'Mimaropa'),
    ('Region V', 'Bicol Region'),
    ('Region VI', 'Western Visayas'),
    ('Region VII', 'Central Visayas'),
    ('Region VIII', 'Eastern Visayas'),
    ('Region IX', 'Zamboanga Peninsula'),
    ('Region X', 'Northern Mindanao'),
    ('Region XI', 'Davao Region'),
    ('Region XII', 'SOCCSKSARGEN'),
    ('Region XIII', 'Caraga'),
    ('NCR', 'National Capital Region'),
    ('CAR', 'Cordillera Administrative Region'),
    ('BARMM', 'Bangsamoro Autonomous Region in Muslim Mindanao'),
    ('NS', 'Zamboanga Peninsula'),
]
CITIES_SELECTION = [
    ('012801','Adams'),
    ('012802','Bacarra'),
    ('012803','Badoc'),
    ('012804','Bangui'),
    ('012805','City of Batac'),
    ('012806','Burgos'),
    ('012807','Carasi'),
    ('012808','Currimao'),
    ('012809','Dingras'),
    ('012810','Dumalneg'),
    ('012811','Banna'),
    ('012812','City of Laoag (Capital)'),
    ('012813','Marcos'),
    ('012814','Nueva Era'),
    ('012815','Pagudpud'),
    ('012816','Paoay'),
    ('012817','Pasuquin'),
    ('012818','Piddig'),
    ('012819','Pinili'),
    ('012820','San Nicolas'),
    ('012821','Sarrat'),
    
]


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
    region= models.CharField(max_length=80, null=True, blank=True)
    barangay= models.CharField(max_length=100, null=True, blank=True)
    city= models.CharField(max_length=100, null=True, blank=True)
    total_of_cave= models.IntegerField(null=True, blank=True)
    type_of_animal = models.CharField(max_length=100, null=True, blank=True)
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


