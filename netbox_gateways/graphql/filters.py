import strawberry_django
from netbox.graphql.filter_mixins import autotype_decorator, BaseFilterMixin

from netbox_gateways.models import Gateway
from netbox_gateways.filtersets import GatewayFilterSet

__all__ = (
    "GatewayFilter",
)


@strawberry_django.filter(Gateway, lookups=True)
@autotype_decorator(GatewayFilterSet)
class GatewayFilter(BaseFilterMixin):
    pass
