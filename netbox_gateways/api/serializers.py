from rest_framework import serializers

from ipam.api.serializers import NestedPrefixSerializer, NestedIPAddressSerializer
from netbox.api.serializers import NetBoxModelSerializer, WritableNestedSerializer
from ..models import Gateway  # , GatewayRule


#
# Nested serializers
#


class NestedGatewaySerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:netbox_gateways-api:gateway-detail",
    )

    class Meta:
        model = Gateway
        fields = ("id", "url", "vrf", "display", "gateway_ip", "prefix")


#
# Regular serializers
#


class GatewaySerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:netbox_gateways-api:gateway-detail",
    )

    prefix = NestedPrefixSerializer()
    gateway_ip = NestedIPAddressSerializer()

    class Meta:
        model = Gateway
        fields = (
            "id",
            "url",
            "display",
            "vrf",
            "gateway_ip",
            "prefix",
            "tags",
            "custom_fields",
            "created",
            "last_updated",
        )
