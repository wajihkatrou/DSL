from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin
from rest_framework import routers
from cities.views import *
from dsl.views import *


router = routers.DefaultRouter()
router.register(r'', CityViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'towns/', include(router.urls)),
    path('sql/', dsl_view, name='dsl-view'),
]
