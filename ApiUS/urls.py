from rest_framework import routers
from .api import ProductoviewSet

router = routers.DefaultRouter()
router.register('api/ApiUS',ProductoviewSet,'ApiUS')

urlpatterns = router.urls