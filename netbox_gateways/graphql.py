from graphene import ObjectType
from netbox.graphql.types import NetBoxObjectType
from netbox.graphql.fields import ObjectField, ObjectListField
from . import filtersets, models


#
# Object types
#


class GatewayType(NetBoxObjectType):
    class Meta:
        model = models.Gateway
        fields = "__all__"


#
# Queries
#


class Query(ObjectType):
    gateway = ObjectField(GatewayType)
    gateways = ObjectListField(GatewayType)


schema = Query
