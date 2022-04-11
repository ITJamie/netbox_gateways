from extras.plugins import PluginTemplateExtension
from ipam.models import Prefix
from .models import Gateway


class IPGatewayTemplate(PluginTemplateExtension):
    model = "ipam.ipaddress"

    def left_page(self):
        return self.x_page()
        return ""

    def x_page(self):
        obj = self.context["object"]
        try:
            gateways_obj = Gateway.objects.get(gateway_ip=obj)
        except Gateway.DoesNotExist:
            gateways_obj = None
        if not gateways_obj:
            meow = 1
            related_prefixs = Prefix.objects.filter(
                vrf=obj.vrf,
                prefix__net_contains_or_equals=str(obj.address.ip),
                status="active",  # Only search for "active" prefixes
            ).prefetch_related("site", "role")
            prefix = related_prefixs[
                len(related_prefixs) - 1
            ]  # get last prefix in the recordset above
        else:
            prefix = gateways_obj.prefix

        if not gateways_obj:
            try:
                gateways_obj = Gateway.objects.get(prefix=prefix)
            except: 
                gateways_obj = None

        return self.render(
            "netbox_gateways/ip_card.html",
            extra_context={
                "meow": "mix",
                "gateways_obj": gateways_obj,
                "prefix": prefix,
            },
        )


class PrefixGatewayTemplate(PluginTemplateExtension):
    model = "ipam.prefix"

    def left_page(self):
        return self.x_page()
        return ""

    def x_page(self):
        obj = self.context["object"]
        try:
            gateways_obj = Gateway.objects.get(prefix=obj)
        except Gateway.DoesNotExist:
            gateways_obj = None

        return self.render(
            "netbox_gateways/prefix_card.html",
            extra_context={
                "prefix": obj,
                "gateways_obj": gateways_obj,
            },
        )


template_extensions = [IPGatewayTemplate, PrefixGatewayTemplate]
