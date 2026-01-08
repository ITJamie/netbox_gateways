import strawberry_django
from netbox.graphql.filters import BaseModelFilter

from netbox_gateways.models import Gateway

__all__ = (
    "GatewayFilter",
)


@strawberry_django.filter(Gateway, lookups=True)
class GatewayFilter(BaseModelFilter):
    pass
