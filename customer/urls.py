from rest_framework import routers
from .views import CustomerViewSet

router = routers.SimpleRouter()
router.register('cus', CustomerViewSet)

urlpatterns = router.urls
