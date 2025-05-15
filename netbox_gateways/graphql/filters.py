import strawberry_django
from netbox.graphql.filter_mixins import BaseFilterMixin

from netbox_gateways.models import Gateway
from netbox_gateways.filtersets import GatewayFilterSet

__all__ = (
    "GatewayFilter",
)


@strawberry_django.filter(Gateway, lookups=True)
class GatewayFilter(BaseFilterMixin):
    pass
