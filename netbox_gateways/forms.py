from django import forms

from ipam.models import Prefix, IPAddress, VRF
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from utilities.forms.fields import CommentField, DynamicModelChoiceField
from .models import Gateway


class GatewayForm(NetBoxModelForm):

    vrf = DynamicModelChoiceField(
        queryset=VRF.objects.all(),
        null_option="Global",
        required=False,
    )
    prefix = DynamicModelChoiceField(
        queryset=Prefix.objects.all(),
        query_params={"vrf_id": "$vrf"},
    )
    gateway_ip = DynamicModelChoiceField(
        queryset=IPAddress.objects.all(),
        query_params={"vrf_id": "$vrf"},
    )

    class Meta:
        model = Gateway
        fields = ("vrf", "prefix", "gateway_ip", "tags")


class GatewayFilterForm(NetBoxModelFilterSetForm):
    model = Gateway
    vrf = DynamicModelChoiceField(
        queryset=VRF.objects.all(),
        null_option="Global",
        required=False,
    )
    prefix = DynamicModelChoiceField(
        queryset=Prefix.objects.all(),
        required=False,
    )
    gateway_ip = DynamicModelChoiceField(
        queryset=IPAddress.objects.all(),
        required=False,
    )
