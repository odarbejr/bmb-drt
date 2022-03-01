# from django.conf.urls import url
# from .import views
from django.urls import path,include
from .router import router

urlpatterns=[
    path('',include(router.urls)),
    # url(r'^layers/$',views.layers),
]