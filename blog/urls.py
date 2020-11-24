from django.urls import path, include
from rest_framework import routers

from . import views
from .views import PostViewSet

router = routers.DefaultRouter()
router.register('post', PostViewSet)

urlpatterns = [
    path('blog/', include(router.urls)),
    ]
