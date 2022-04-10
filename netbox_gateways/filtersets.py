from netbox.filtersets import NetBoxModelFilterSet
from .models import Gateway
from utilities.forms.fields import CommentField, DynamicModelChoiceField
from ipam.models import Prefix, IPAddress, VRF


class GatewayFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = Gateway
        fields = ("id", "vrf", "prefix", "gateway_ip")

    def search(self, queryset, name, value):
        return queryset.filter(description__icontains=value)
