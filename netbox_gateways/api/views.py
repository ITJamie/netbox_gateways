from django.db.models import Count

from netbox.api.viewsets import NetBoxModelViewSet

from .. import filtersets, models
from .serializers import GatewaySerializer  # , GatewayRuleSerializer


class GatewayViewSet(NetBoxModelViewSet):
    queryset = models.Gateway.objects.all()
    serializer_class = GatewaySerializer
    filterset_class = filtersets.GatewayFilterSet
