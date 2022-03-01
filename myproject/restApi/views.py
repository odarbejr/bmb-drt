from django.shortcuts import render
from rest_framework import viewsets
# from rest_framework.authtoken.views import ObtainAuthToken
# from rest_framework.authtoken.models import Token
# from rest_framework.response import Response
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.decorators import authentication_classes, permission_classess


from .serializers import caveinventorySerializer
from .serializers import Period_accessmentSerializer
from .serializers import Geographic_descriptionSerializer
from .serializers import climatological_dataSerializer
from .serializers import excisting_land_useSerializer
from .serializers import demographic_informationSerializer
from .serializers import usesSerializer
from .serializers import Layers_attributeSerializer
from .serializers import citiesSerializer

from .models import caveinventory
from .models import Period_accessment
from .models import Geographic_description
from .models import climatological_data
from .models import excisting_land_use
from .models import demographic_information
from .models import uses
from .models import Layers_attribute
from .models import cities




# @authentication_classes([TokenAuthentication])
# @permission_classess([IsAuthenticated])
# class CustomAuthTokenLogin(ObtainAuthToken):

#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data,
#                                            context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({
#             'token': token.key,
#             'user_id': user.pk,
#             'username': user.username,
#             'first_name': user.first_name,
#             'last_name': user.last_name,
#         })


class caveinventory_viewset(viewsets.ModelViewSet):
    queryset=caveinventory.objects.all()
    serializer_class=caveinventorySerializer

class Period_accessment_viewset(viewsets.ModelViewSet):
    queryset=Period_accessment.objects.all()
    serializer_class=Period_accessmentSerializer

class Geographic_description_viewset(viewsets.ModelViewSet):
    queryset=Geographic_description.objects.all()
    serializer_class=Geographic_descriptionSerializer

class climatological_data_viewset(viewsets.ModelViewSet):
    queryset=climatological_data.objects.all()
    serializer_class=climatological_dataSerializer

class excisting_land_use_viewset(viewsets.ModelViewSet):
    queryset=excisting_land_use.objects.all()
    serializer_class=excisting_land_useSerializer

class demographic_information_viewset(viewsets.ModelViewSet):
    queryset=demographic_information.objects.all()
    serializer_class=demographic_informationSerializer

class uses_viewset(viewsets.ModelViewSet):
    queryset=uses.objects.all()
    serializer_class=usesSerializer
    
class Layers_attribute_viewset(viewsets.ModelViewSet):
    queryset=Layers_attribute.objects.all()
    serializer_class=Layers_attributeSerializer



class cities_viewset(viewsets.ModelViewSet):
    queryset=cities.objects.all()
    serializer_class=citiesSerializer

# def layers(request):
#     layers=Layers_attribute.objects.all()
#     return render(request,'restApi/layers_list.html',{'layers':'layers'})