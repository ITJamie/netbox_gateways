from typing import List

import strawberry
import strawberry_django

from netbox_gateways.models import Gateway

from .types import GatewayType


@strawberry.type(name="Query")
class NetBoxGatewayQuery:
    gateway: GatewayType = strawberry_django.field()
    gateway_list: List[GatewayType] = strawberry_django.field()
