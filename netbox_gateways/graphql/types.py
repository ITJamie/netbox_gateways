from typing import Annotated

import strawberry
import strawberry_django

from netbox.graphql.types import NetBoxObjectType

from netbox_gateways.models import Gateway
from .filters import GatewayFilter


@strawberry_django.type(Gateway, fields="__all__", filters=GatewayFilter)
class GatewayType(NetBoxObjectType):
    vrf: Annotated["VRFType", strawberry.lazy("ipam.graphql.types")] | None
    prefix: Annotated["PrefixType", strawberry.lazy("ipam.graphql.types")]
    gateway_ip: Annotated["IPAddressType", strawberry.lazy("ipam.graphql.types")]
