import django_tables2 as tables

from netbox.tables import NetBoxTable, ChoiceFieldColumn
from .models import Gateway  # , GatewayRule


class GatewayTable(NetBoxTable):
    prefix = tables.Column(linkify=True)
    vrf = tables.Column(linkify=True)
    gateway_ip = tables.Column(linkify=True)

    class Meta(NetBoxTable.Meta):
        model = Gateway
        fields = ("pk", "id", "vrf", "prefix", "gateway_ip", "actions")
        default_columns = ("id", "vrf", "prefix", "gateway_ip")
