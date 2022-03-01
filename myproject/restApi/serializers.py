from rest_framework import serializers
from .models import caveinventory
from .models import Period_accessment
from .models import Geographic_description
from .models import climatological_data
from .models import excisting_land_use
from .models import demographic_information
from .models import uses
from .models import Layers_attribute
from .models import cities

class caveinventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = caveinventory
        fields='__all__'

class Period_accessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period_accessment
        fields='__all__'

class Geographic_descriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geographic_description
        fields='__all__'

class climatological_dataSerializer(serializers.ModelSerializer):
    class Meta:
        model = climatological_data
        fields='__all__'

class excisting_land_useSerializer(serializers.ModelSerializer):
    class Meta:
        model = excisting_land_use
        fields=['listing_by_type', 'adjacent_to_cave', 'above_cave']

class demographic_informationSerializer(serializers.ModelSerializer):
    class Meta:
        model = demographic_information
        fields=['name_brgy', 'population', 'households', 'families', 'livelihood', 'others']

class usesSerializer(serializers.ModelSerializer):
    class Meta:
        model = uses
        fields='__all__'

class Layers_attributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Layers_attribute
        fields=[
            'id', 
            'layer_name', 
            'description', 
            'region', 
            'barangay', 
            'city', 
            'total_of_cave', 
            'type_of_animal', 
            'total_of_male',
            'total_of_female',
            'overall_gender',
            'size',
            'color',
            'remarks'
        ]
class citiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = cities
        fields=[
            'name'  
        ]