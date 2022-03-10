from rest_framework import routers
from .views import caveinventory_viewset
from .views import Period_accessment_viewset
from .views import Geographic_description_viewset
from .views import climatological_data_viewset
from .views import excisting_land_use_viewset
from .views import demographic_information_viewset
from .views import uses_viewset
from .views import Layers_attribute_viewset
from .views import cities_viewset
from .views import region_viewset
from .views import Type_of_animals_viewset

router=routers.DefaultRouter()
router.register('caveinventory',caveinventory_viewset)
router.register('Period_accessment',Period_accessment_viewset)
router.register('Geographic_description',Geographic_description_viewset)
router.register('climatological_data',climatological_data_viewset)
router.register('excisting_land_use',excisting_land_use_viewset)
router.register('demographic_information',demographic_information_viewset)
router.register('uses',uses_viewset)
router.register('Layers_attribute',Layers_attribute_viewset)
router.register('region',region_viewset)
router.register('cities',cities_viewset)
router.register('Type_of_animals',Type_of_animals_viewset)


""""
PUT-UPDATE
GET- RETRIEVE / LIST SHOWING
POST- CREATE
DELETE-delete

"""