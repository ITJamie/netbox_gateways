from netbox.api.routers import NetBoxRouter
from . import views


app_name = "netbox_gateway"

router = NetBoxRouter()
router.register("gateway", views.GatewayViewSet)

urlpatterns = router.urls
