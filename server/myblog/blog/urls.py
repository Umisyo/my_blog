from rest_framework import routers
from .views import UserViewSet, BlogViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('blogs', BlogViewSet)

