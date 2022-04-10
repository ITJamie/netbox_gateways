from django.db.models import Count

from netbox.views import generic
from . import filtersets, forms, models, tables


#
# Gateway views
#


class GatewayView(generic.ObjectView):
    queryset = models.Gateway.objects.all()
    permission_required = "netbox_gateways.view_gateway"


class GatewayListView(generic.ObjectListView):
    queryset = models.Gateway.objects.all()
    table = tables.GatewayTable
    filterset = filtersets.GatewayFilterSet
    filterset_form = forms.GatewayFilterForm
    permission_required = "netbox_gateways.view_gateway"


class GatewayEditView(generic.ObjectEditView):
    queryset = models.Gateway.objects.all()
    form = forms.GatewayForm
    permission_required = "netbox_gateways.addedit_gateway"


class GatewayDeleteView(generic.ObjectDeleteView):
    queryset = models.Gateway.objects.all()
    permission_required = "netbox_gateways.delete_gateway"
