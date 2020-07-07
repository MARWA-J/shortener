from rest_framework import routers
from backend.api import ShortenerViewSet

router = routers.DefaultRouter()
router.register('api/v1.0/shortener', ShortenerViewSet, 'shortener')

urlpatterns = router.urls
