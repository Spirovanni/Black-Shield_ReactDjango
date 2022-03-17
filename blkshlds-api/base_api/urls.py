from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import CardViewSet, RatingViewSet

router = routers.DefaultRouter()
router.register('cards', CardViewSet)
router.register('ratings', RatingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]