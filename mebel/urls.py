from django.urls import path, include
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from .views import AllView,SavatView

router = routers.DefaultRouter()
router.register(r'alldata', AllView, basename='alldata')
router.register(r'savat',SavatView,basename='savat')
# router.register(r'')



urlpatterns = [
    path('', include(router.urls)),
    path('schema/',get_schema_view(title='Api schema',version='1.0.0',description='Online shop'))
]

